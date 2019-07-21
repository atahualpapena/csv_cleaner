import boto3
import os
import sys
import uuid

s3_client = boto3.client('s3')


def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/cleaned-{}{}'.format.key

        s3_client.download_file(bucket, key, download_path)

        with open(download_path) as
        file_in, open(upload_path, 'w+')
        as file_out:
            for line_num in range(4):
                next(file_in)

            for line in file_in:
                file_out.write(line)

        s3_client.upload_file(
            upload_path, 'my_bucket_name'.format(bucket), key)
