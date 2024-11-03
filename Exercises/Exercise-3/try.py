import boto3, botocore

# Create an S3 client without authentication
s3 = boto3.client('s3', 'US-East-1', config=botocore.client.Config(signature_version=botocore.UNSIGNED))

# List files in the commoncrawl bucket
response = s3.list_objects_v2(Bucket='commoncrawl', Prefix='crawl-data/')
for obj in response.get('Contents', []):
    print(obj['Key'])

# Download a specific file
s3.download_file('commoncrawl', 'crawl-data/CC-MAIN-2023-26/segments/12345.warc.gz', 'local_file.warc.gz')