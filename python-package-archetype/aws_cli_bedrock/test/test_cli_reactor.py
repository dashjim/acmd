import os
import sys
from unittest import TestCase

from aws_cli_bedrock.cli_reactor import invoke

# Add project root to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


print(">> start")


class TestInvoke(TestCase):
    """
    TODO Add more tests here.
    """

    def test_invoke(self):
        sys.argv = ["acmd", "please", "list", "all",
                    "my", "s3", "buckets", "in", "us-east-2."]
        sys.argv = ["amcd", "列出我在us-east-2的全部s3桶。"]
        sys.argv = ["acmd", "列出正在运行的Ec2实例。"]
        sys.argv = ["amcd", "查一下我所有的codecommit repo, 按字符过滤包含aws的"]
        result = invoke()
        assert len(result) > 0
