import json
import urllib3
import boto3
from datetime import datetime

#connect to S3 bucket with the boto3 client
s3 = boto3.client('s3')

#the function is executed when the lambda is invoked
def lambda_handler(event, context):

    #AWS does not support the requests library so urllib3 must be imported and used as a http client
    http = urllib3.PoolManager()

    #get the text data from the API
    api_data = http.request('GET', 'API Link')

    #convert it to a JSON dictionary
    data = json.loads(api_data.data)

    #datetime for the unique file name
    dateTimeObj = datetime.now()

    #put the file into the S3 bucket(insert your bucket name)
    s3.put_object(Body=json.dumps(data).encode('UTF-8'), Bucket='your_bucket_name',Key='load/continents '+str(dateTimeObj)+'.json', ContentType='application/json')

    return 'JSON file uploaded to S3 bucket'
