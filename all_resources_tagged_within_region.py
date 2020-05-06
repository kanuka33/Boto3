#Returns all the tagged or previously tagged resources that are located in the specified Region for the AWS account.

import boto3
aws_man=boto3.session.Session(profile_name="root")
res_api=aws_man.client('resourcegroupstaggingapi', 'us-east-1')
response=res_api.get_resources()
for each_item in response['ResourceTagMappingList']:
    print(each_item['ResourceARN'], each_item['Tags'])
