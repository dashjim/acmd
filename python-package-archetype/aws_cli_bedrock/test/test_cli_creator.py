from unittest import TestCase
import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  

from aws_cli_bedrock.cli_creactor import invoke


print(">> start")
class TestInvoke(TestCase):
    """
    TODO Add more tests here.
    """

    def test_invoke(self):
        sys.argv = ["acbr", "please", "list", "all", "my", "s3", "buckets", "in", "us-east-2." ]
        # sys.argv = ["acbr", "列出我在us-east-2的全部s3桶。"]
        sys.argv = ["acbr", "列出正在运行的Ec2实例。"]
        sys.argv = ["acbr", "列出我在codecommit上的repo."]
        result = invoke()
        assert len(result) > 0
