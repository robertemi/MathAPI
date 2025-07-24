from models.MathAPI import MathAPI
import json


class Power(MathAPI):
    def __init__(self):
        super().__init__()

    '''
    Computes the given power of the given number

    '''

    def compute(self, number, power):
        result = 1

        for i in range(abs(power)):
            result = result * number

        if power < 0:
            return 1 / result
        else:
            return result

    @classmethod
    def save(cls, conn, method, status_code, request_body, response_body):
        print(f'Received-> method: {method}, status_code: {status_code},'
              'request_body: {request_body}, response_body :{response_body}')
        try:
            with conn.cursor() as cur:
                cur.execute(
                    'INSERT INTO api_requests '
                    '(method, status_code, request_body, '
                    'response_body, operation)'
                    'VALUES (%s, %s, %s, %s, %s) RETURNING id',
                    (
                        method,
                        status_code,
                        json.dumps(request_body),
                        json.dumps(response_body),
                        'Power'
                    )
                )
                result = cur.fetchone()
                if not result:
                    print("No ID returned from INSERT")
                    return None

                request_id = result[0]
                conn.commit()
                print(f"Successfully saved power request: {request_id}")
        except Exception as e:
            conn.rollback()
            print(f"General error in Power.save(): {e}")
