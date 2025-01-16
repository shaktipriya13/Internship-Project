import json

def lambda_handler(event, context):
    try:
        # Extract numbers from the event
        num1 = event.get('num1')
        num2 = event.get('num2')

        # Validate that both inputs are numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Both num1 and num2 must be numbers.")

        # Perform the addition
        result = num1 + num2

        # Return a successful response with the result
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'The result of adding {num1} and {num2} is {result}',
                'result': result
            })
        }

    except Exception as e:
        # Return an error response if input is invalid
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': str(e)
            })
        }
