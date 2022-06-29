'''
Task: Collect assest information and upload to S3 bucket
'''

import platform
import time
import json
import boto3

ts = time.time()

details = {'Timestamp': ts,
           'Node': platform.node(),
           'Architecture': platform.architecture(),
           'Machine': platform.machine(),
           'System': platform.system(),
           'Kernal release': platform.release(),
           'Kernal debian package name': platform.platform(),
           'Kernal debian package version': platform.version()}

Filename_txt = 'asset'+str(ts)+'.txt'

with open(Filename_txt, 'w', encoding='utf-8') as convert_file:
    convert_file.write(json.dumps(details))


# 3. Connect to s3 bucket and upload the file
s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-3',
    aws_access_key_id='accessid',
    aws_secret_access_key='accesskey'
)

# buckets available 
for bucket in s3.buckets.all():
    print(bucket.name)

s3.Bucket('demo-asset-info').upload_file(Filename=Filename_txt, Key=Filename_txt)
print("File uploaded to S3 bucket.")