import boto3
import time
import json


sqs = boto3.client('sqs', region_name='us-east-1')


queue_url = 'https://sqs.us-east-1.amazonaws.com/654654419570/MyQueue'

while True:
    
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=10  
    )

    if 'Messages' in response:
        for message in response['Messages']:
            
            content = json.loads(message['Body'])
            print(f"Processing message: {content}")

         
            receipt_handle = message['ReceiptHandle']
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)


    time.sleep(60)
