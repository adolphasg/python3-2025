import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='agwena-boto3-05052025',
   
)

print(response)

