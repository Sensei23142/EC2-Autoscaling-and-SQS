import boto3
import json

sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/654654419570/MyQueue'


message_body = {
    "vehicleId": "VH2001",
    "make": "Honda",
    "model": "Civic",
    "year": 2020,
    "color": "Blue",
    "mileage": 15000
}

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(message_body)
)
