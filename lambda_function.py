import json

def lambda_handler(event, context):
    print("Real-time file received")

    return {
        'statusCode': 200,
        'body': json.dumps('Processing Complete')
    }
