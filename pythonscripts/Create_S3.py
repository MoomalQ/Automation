"""
Create an S3 bucket using python
"""
import boto3

AWS_REGION = "eu-west-3"
resource = boto3.resource("s3", region_name=AWS_REGION)
BUCKET_NAME = "demo-s3-2022"
location = {'LocationConstraint': AWS_REGION}
bucket = resource.create_bucket(
    Bucket=BUCKET_NAME,
    CreateBucketConfiguration=location)
print("Amazon S3 bucket has been created")