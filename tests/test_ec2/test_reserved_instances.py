import boto
import sure  # noqa

from moto import mock_ec2


@mock_ec2
def test_reserved_instances():
    pass
