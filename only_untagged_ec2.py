import boto3
import sys
import pprint
aws_man=boto3.session.Session(profile_name="root")
client = aws_man.client('ec2', 'us-east-1')
response = client.describe_instances()

obj_number = len(response['Reservations'])

for objects in range(obj_number):
    try:
        z = response['Reservations'][objects]['Instances'][0]['Tags'][0]['Key']
    except KeyError as e:
        untagged_instanceid = response['Reservations'][objects]['Instances'][0]['InstanceId']
        untagged_state = response['Reservations'][objects]['Instances'][0]['State']['Name']
        print("InstanceID: {0}, RunningState: {1}".format(untagged_instanceid, untagged_state))
