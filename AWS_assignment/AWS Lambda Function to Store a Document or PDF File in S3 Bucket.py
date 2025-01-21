# AWS Lambda Function Code to Store a Document or PDF File in S3 Bucket 
import json
import boto3
import csv
import io

s3Client = boto3.client('s3')

def lambda_handler(event, context): 
    # Get the bucket and file name from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
  
    print(f"Bucket: {bucket}")
    print(f"Key: {key}")
  
    # Get the object from S3
    response = s3Client.get_object(Bucket=bucket, Key=key)
  
    # Process the object
    data = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader)  # Skip the header row
    for row in reader: 
        print(f"Year - {row[0]}, Mileage - {row[1]}, Price - {row[2]}")
