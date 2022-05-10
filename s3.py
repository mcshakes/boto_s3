import logging
import boto3
from botocore.exceptions import ClientError

class S3Client:
    def __init__(self, session, region_name = "us-east-1"):
        self.client = session.client("s3", region_name=region_name)
    
    def list_buckets(self):
        response = self.client.list_buckets()
        print('Existing buckets:')
        print("*" * 30)
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

# def list_buckets(session):
#     s3 = session.client('s3')
#     response = s3.list_buckets()

#     # Output the bucket names
#     print('Existing buckets:')
#     print("*" * 30)
#     for bucket in response['Buckets']:
#         print(f'  {bucket["Name"]}')


# s3_resource = boto3.resource('s3')
# s3_client = boto3.client('s3')


# def create_bucket(session, bucket_name, region=None):
#     """Create an S3 bucket in a specified region

#     If a region is not specified, the bucket is created in the S3 default
#     region (us-east-1).

#     :param session: Profile Session 
#     :param bucket_name: Bucket to create
#     :param region: String region to create bucket in, e.g., 'us-west-2'
#     :return: True if bucket created, else False
#     """

#     # Create bucket
#     try:
#         if region is None:
#             s3_client = boto3.client('s3')
#             s3_client.create_bucket(Bucket=bucket_name)
#         else:
#             s3_client = boto3.client('s3', region_name=region)
#             location = {'LocationConstraint': region}
#             s3_client.create_bucket(Bucket=bucket_name,
#                                     CreateBucketConfiguration=location)
#     except ClientError as e:
#         logging.error(e)
#         return False

#     return True

# def get_bucket_policy(name: str, session):
#     s3 = session.client('s3')
#     return s3.get_bucket_policy(Bucket=name)