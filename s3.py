import logging
import boto3
import json
from botocore.exceptions import ClientError

class S3Client:
    def __init__(self, session, region_name = None):
        self.client = session.client("s3", region_name=region_name)
        self.region_name = region_name
        
    def list_buckets(self):
        response = self.client.list_buckets()
        print('Existing buckets:')
        print("*" * 30)

        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

    def get_bucket_policy(self, name: str):
        try:            
            policy = self.client.get_bucket_policy(Bucket=name)
            print(policy)
        except ClientError as e:
            logging.error(e)
            return False

    def add_bucket_policy(self, bucket_policy, bucket_name: str):
        new_policy = bucket_policy
        new_policy["Statement"][0]["Resource"] = f"arn:aws:s3:::{bucket_name}/*"
        policy_string = json.dumps(new_policy)

        self.client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=policy_string
        )

    def allow_public_access(self, bucket_name: str):
        self.client.put_public_access_block(
            Bucket=bucket_name,
            # ContentMD5='string',
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )

    def create_bucket(self, bucket_name: str, region_name: str = None):
        """
        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """

        try:
            if region_name is None:
                self.client.create_bucket(Bucket=bucket_name)
            else:
                location = {'LocationConstraint': region_name}
                self.client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False

        return True  






