import psycopg2
from models.MathAPI import MathAPI


class Factorial(MathAPI):
    def __init__(self):
        super(MathAPI)

    def compute(self, number):
        return 1 if number <= 1 else number * self.compute(number - 1)

    @classmethod
    def save(cls, conn, method, status_code, request_body, response_body):
        try:
            with conn.cursor() as cur:
                cur.execute(
                    'INSERT INTO api_requests '
                    '(method, status_code, request_body, response_body, operation)'
                    'VALUES (%s, %s, %s, %s, %s) RETURNING id',
                    (method, status_code, request_body, response_body, 'Factorial')
                )
                result = cur.fetchone()
                if not result:
                    print("No ID returned from INSERT")
                    return None

                request_id = result[0]
                conn.commit()
                print(f"Successfully saved factorial request: {request_id}")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Database error in Factorial.save(): {e.pgerror}")
            print(f"Database error code: {e.pgcode}")
            return None
