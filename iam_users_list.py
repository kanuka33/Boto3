# Listing all IAM Users

import boto3
aws_man=boto3.session.Session(profile_name="root")
iam_con=aws_man.client(service_name="iam",region_name="us-east-1")
for user in iam_con.list_users()['Users']:
    print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
    user['UserName'],
    user['UserId'],
    user['Arn'],
    user['CreateDate'],
    user.get('Tags',None)
        )
    )
    
 
