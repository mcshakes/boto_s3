import boto3
from s3 import list_buckets


# If you try to create a bucket, but another user has already claimed your desired bucket name, your code will fail. Instead of success, you will see the following error: botocore.errorfactory.BucketAlreadyExists.


def create_boto_session():
    return boto3.Session(profile_name='boto3-dev')

session = create_boto_session()

# create_bucket(session, "werkerpeeper")
list_buckets(session)
# sts = session.client('sts')
# print(sts.get_caller_identity())
