import boto3
from s3 import S3Client


bucket_policy = {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "AddPerm",
                            "Principal": "*",
                            "Effect": "Allow",
                            "Action": "s3:GetObject",
                            
                        }
                    ]
                }

                # "Resource": "arn:aws:s3:::www.somethingsimple.io/*"
def create_boto_session():
    return boto3.Session(profile_name='boto3-dev')
    

session = create_boto_session()

# create_bucket(session, "werkerpeeper")
client = S3Client(session)
# client.create_bucket("werkerpeeper")
# client.add_bucket_policy(bucket_policy, "werkerpeeper")
# client.allow_public_access('werkerpeeper')
# client.list_buckets()
client.get_bucket_policy('werkerpeeper')
# sts = session.client('sts')
# print(sts.get_caller_identity())

