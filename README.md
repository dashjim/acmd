# acmd - run aws-cli with natural language.

This a package use BedRock LLM to automatically generate the AWS CLI and execute it.

> This is still a early reversion: `USE AT YOUR OWN RISK`.


[![Watch the video](https://youtu.be/c1xR3Anheqs)](https://youtu.be/c1xR3Anheqs)

**Example Usage**

Usage:  
    
`acmd [action] [prompt]` 


Actions:

          The first verb after `acmd` is deemed as an action. Possible verbs are:

          dryrun - TODO only generate the AWS-CLI command, do not run it.
          clear - TODO clear chat history
          upload - TODO I case you have wrong generation. Upload history prompt and bedrock respond to the maintenance team to analyze. 
                        Recommend to clear none related chat history first, then only upload problematic interactions.
Example:

          acmd list all my s3 buckets. 
          acmd dryrun list all my s3 buckets.

### Contribute

We really need your contribution in the following types:

* Report issues.
* Raise your new feature request at the issues.
* Send RP to us.
* Join the AWS internal slack channel `acmd-interest` if you are an amazonian.
