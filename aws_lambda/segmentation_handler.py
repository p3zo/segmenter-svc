import boto3
import io

from segmenter.segmenter import segment_file

S3_BUCKET = "p3zo-segmenter"


def get_s3_client():
    return boto3.client("s3")


def get_from_bucket(key, bucket):
    print(f"Downloading {key} from {bucket}...")
    rtn = io.BytesIO()
    get_s3_client().download_fileobj(Bucket=bucket, Key=key, Fileobj=rtn)
    rtn.seek(0)
    return rtn


def segmentation_handler(event, context):
    s3_key = event["Records"]["s3"]["object"]["key"]
    file_obj = get_from_bucket(s3_key, bucket=S3_BUCKET)
    segmentation = segment_file(file_obj)
    return segmentation
