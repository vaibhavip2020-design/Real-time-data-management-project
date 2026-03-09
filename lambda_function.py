import json

def lambda_handler(event, context):
    print("File uploaded to S3 successfully")

    return {
        'statusCode': 200,
        'body': json.dumps('Real-time processing complete')
    }
