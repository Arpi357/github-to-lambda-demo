def handler(event, context):
    message = "Hello Arpitha 👋, your Lambda is running from GitHub!"
    print(message)  # This will be logged to CloudWatch
    return {
        "statusCode": 200,
        "body": message
    }
