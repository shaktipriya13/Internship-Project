# AWS Lambda Function Code to Store a Document or PDF File in S3 Bucket 
import json
import boto3
import csv
import io
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3Client = boto3.client('s3')

def lambda_handler(event, context): 
    try:
        # Get the bucket and file name from the event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
      
        logger.info(f"Bucket: {bucket}")
        logger.info(f"Key: {key}")
      
        # Get the object from S3
        response = s3Client.get_object(Bucket=bucket, Key=key)
      
        # Process the object
        data = response['Body'].read().decode('utf-8')
        reader = csv.reader(io.StringIO(data))
        next(reader, None)  # Skip the header row, if it exists

        for row in reader: 
            logger.info(f"Year - {row[0]}, Mileage - {row[1]}, Price - {row[2]}")

    except KeyError as e:
        logger.error(f"Key error: {str(e)}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

