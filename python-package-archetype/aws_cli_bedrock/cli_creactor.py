import boto3
import subprocess
import json
import sys

bedrock = boto3.client(service_name='bedrock-runtime')

CONST_CLINT_SIDE_ERROR = "client_side_error"

def invoke():
    """
    Usage: acbr please list all my s3 buckets. 
    """
    if len(sys.argv) > 1:

        # print(sys.argv)

        ## concat all values in sys.argv into one value.
        sys.argv.pop(0)
        client_query = " ".join(sys.argv)
        print(f"> Query: {client_query}")

        return start_agent_flow(client_query)
    else:
        print("Usage: acbr please list all my s3 buckets. ")

def start_agent_flow(query):
    """
    TODO: Design the agent interface (input and output).
    """
    generated_instruction = agent_bedrock(query)
    return agent_aws_cli(generated_instruction)

def agent_aws_cli(instruction):
    # print(instruction.strip().split(" "))
    print("Running...\n")
    result = subprocess.run(instruction.strip().split(" "), capture_output=True) 
    result_str = result.stdout.decode().replace("\\n","\n")
    print(result_str)
    return result_str

def get_complete_prompt(query):
    full_prompt = f"""
            You are a helpful technical professional, you will convert the human query into aws cli commands.  
            Please pay attention to the correctness of the generated command.
            Here are the examples you can learn from:
                Query: "List all my s3 buckets."  
                Respond: "aws s3 ls" with no explanations.
                Query: 列出正在运行的Ec2实例。
                Respond: aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query Reservations[*].Instances[*].[InstanceId]
            Notice that the quotes MUST NOT be included in --filters and --query. So it is WRONG to output anything like: --query 'Reservations[*].Instances[*].[InstanceId]'
            
            During the genearation here are rules you should follow:
                1. Please think step by step during the generation.
                2. User inputs may have typo. You need to consider that.
                3. If the question does not lead to aws cli commands generation, you should respond "{CONST_CLINT_SIDE_ERROR}".
                    For example: when asked "Could you tell me who you are?", you should respond "{CONST_CLINT_SIDE_ERROR}".
            Now the human input is: {query}
        """
    return json.dumps({
            "prompt": f"\n\nHuman:{full_prompt} \n\nAssistant:",
            "max_tokens_to_sample": 300,
            "temperature": 0.1,
            "top_p": 0.9,
        })

def agent_bedrock(query):
    """
    Send the query to bedrock.
    TODO: handle the bedrock error and rejections from bedrock.
    """
    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model_with_response_stream(body=get_complete_prompt(query), modelId=modelId, accept=accept, contentType=contentType)
    # print(response)
    response_body = response.get('body')


    # Iterate over events in the event stream as they come
    final_response = ""
    for event in response_body:
        # If we received a records event, write the data to a file
        # print(f">> {event}")
        data = json.loads(event['chunk']['bytes'])
        # print(data['completion'], end='')

        final_response = final_response + data['completion']                
        # If we received a progress event, print the details
        if data['stop_reason'] != None:
            # print(data['stop_reason'])
            continue
    print(f"< bedrock response: {final_response}")
    return final_response 


if __name__ == "__main__":
    sys.argv = ["acbr", "please", "list", "all", "my", "s3", "buckets", "in", "us-east-2." ]
    # sys.argv = ["acbr", "列出我在us-east-2的全部s3桶。"]
    sys.argv = ["acbr", "列出正在运行的Ec2实例。"]
    sys.argv = ["acbr", "列出我在codecommit上的repo."]
    invoke()