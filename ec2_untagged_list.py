import boto3
aws_man=boto3.session.Session(profile_name="root")
ec2_con=aws_man.client(service_name="ec2",region_name="us-east-1")
response=ec2_con.describe_instances()
for each_item in response['Reservations']:
    for each in each_item['Instances']:
        #print(each.get('InstanceId',None),each.get('ImageId',None),each.get('InstanceType',None),each.get('KeyName',None), each['State']['Name'])
        print(each.get('InstanceId',None),each.get('ImageId',None),each.get('InstanceType',None),each['State']['Name'],each.get('Tags',None))
