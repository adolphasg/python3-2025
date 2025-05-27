import boto3

def stop_instances():
    ec2 = boto3.client('ec2')
    
    # Describe all instances
    response = ec2.describe_instances(
        Filters=[{
            'Name': 'instance-state-name',
            'Values': ['running']
        }]
    )
    
    # Get the instance IDs of all running instances
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    # Stop all running instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")
        return f"Stopped instances: {instance_ids}"
    else:
        print("No running instances found.")
        return "No running instances found."

# Lambda requires this handler function
def lambda_handler(event, context):
    return stop_instances()
