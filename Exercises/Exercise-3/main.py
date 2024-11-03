from boto3 import *
import botocore.client

gz_pref = "crawl-data/"
gz_name = "wet.paths.gz"

def main():
    s3 = client('s3', 'us-east-1', config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    objects_list = s3.list_objects_v2(Bucket="commoncrawl", Prefix=gz_pref)
    print(f"{objects_list = }")
    
if __name__ == "__main__":
    main()