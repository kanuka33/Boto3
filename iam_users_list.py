# Listing all IAM Users

import boto3
aws_man=boto3.session.Session(profile_name="root")
iam_con=aws_man.client(service_name="iam",region_name="us-east-1")
for user in iam_con.list_users()['Users']:
    print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
    user['UserName'],
    user['UserId'],
    user['Arn'],
    user['CreateDate']
        )
    )
    

    
<================================================================================================================>    
    
    
    
    
#Listing all IAM users within orginization
import boto3
aws_man=boto3.session.Session(profile_name="root")
iam=aws_man.client(service_name="iam",region_name="us-east-1")
paginator = iam.get_paginator('list_users')
for page in paginator.paginate():
    for user in page['Users']:
        print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
        user['UserName'],
        user['UserId'],
        user['Arn'],
        user['CreateDate']
        )
    )

        
        
        
<==============================================================================================================>
#Creating a User and Assigning Policies in cli

>>>import boto3
>>>aws_man=boto3.session.Session(profile_name="root")
>>>iam=aws_man.client(service_name="iam",region_name="us-east-1")
>>># create a user
...iam.create_user( UserName='prashanth')

>>># attach a policy
>>>iam.attach_user_policy(
 ...UserName = 'prashanth', 
 ...PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)



<==============================================================================================================>

#Listing All User Permissions

import boto3
aws_man=boto3.session.Session(profile_name="root")
iam=aws_man.client(service_name="iam",region_name="us-east-1")
for user_detail in iam.get_account_authorization_details(Filter=['User'])['UserDetailList']:
    policyname = []
    policyarn = []
 # find each policy attached to the user
    for policy in user_detail['AttachedManagedPolicies']:
        policyname.append(policy['PolicyName'])
        policyarn.append(policy['PolicyArn'])
 # print user details 
        print("User: {0}\nUserID: {1}\nPolicyName: {2}\nPolicyARN: {3}\n".format(
        user_detail['UserName'],
        user_detail['UserId'],
        policyname,
        policyarn
            )
        )



