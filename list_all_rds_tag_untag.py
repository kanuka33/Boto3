#!/usr/bin/env python
import boto3
from pprint import pprint
aws_man=boto3.session.Session(profile_name="root")
rds = aws_man.client('rds',"us-east-1")
dbs = rds.describe_db_instances()
for db in dbs['DBInstances']:
    response = rds.list_tags_for_resource(ResourceName=db['DBInstanceArn'])
    print (db['DBInstanceIdentifier'],db['DBInstanceClass'],db['Engine'],db['DBInstanceStatus'],db['DBInstanceArn'], response['TagList'],)

