import boto3

from base import Buckets


class AWSS3(Buckets):
    def __init__(self, **kwargs):
        self.aws_access_key_id = kwargs["aws_access_key_id"]
        self.aws_secret_access_key = kwargs["aws_secret_acess_key"]
        self.bucket_name = kwargs["bucket_name"]
        self.s3 = boto3.resource("s3")

    def push(self):
        data = None ## Read some data
        self.s3.Bucket(self.bucket_name).put_object(Key="test.jpg", Body=data)

    def pull(self):
        pass
    # Code to pull data