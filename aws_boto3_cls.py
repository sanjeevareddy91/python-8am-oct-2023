# boto3 - - pip install boto3

import boto3

s3_client = boto3.client('s3',aws_access_key_id='',aws_secret_access_key='')


# print(s3_client)

# print(dir(s3_client))

# bucket_creation = s3_client.create_bucket(Bucket='python8amdec')

# print(bucket_creation)

# for ele in ['databases_cls.py','databases.txt','Functions_cls.py']:
#     s3_client.upload_file(ele,'python8amdec',ele)

# List Buckets in S3..
# buc_list = [ele['Name'] for ele in s3_client.list_buckets()['Buckets']]

# bucket_name = input("Enter bucket name:")

# if bucket_name in buc_list:
#     print("Bucket already exist")
# else:
#     bucket_creation = s3_client.create_bucket(Bucket=bucket_name)

# print(s3_client.list_objects(Bucket='python8amdec')['Contents'])

# file_list = [ele['Key'] for ele in s3_client.list_objects(Bucket='python8amdec')['Contents']]

# print(file_list)

# s3_client.download_file('python8amdec','control_flow_statements_cls.py','C:/Users/reddy/Downloads/control_flow.py')


# delete object
# for ele in file_list:
#     s3_client.delete_object(Bucket='python8amdec',Key=ele)

s3_client.delete_bucket(Bucket='python8amdec')