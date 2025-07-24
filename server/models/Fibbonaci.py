import psycopg2
from models.MathAPI import MathAPI


class Fibbonaci(MathAPI):
    def __init__(self):
        super(MathAPI)

    '''
    Computes the n_th fibbonaci number

    '''
    def compute(self, n):
        a = 0
        b = 1
        i = 1

        while i < n:
            c = a + b
            a = b
            b = c
            i += 1

        return c

    @classmethod
    def save(cls, conn, method, status_code, request_body, response_body):
        try:
            with conn.cursor() as cur:
                cur.execute(
                    'INSERT INTO api_requests '
                    '(method, status_code, request_body, response_body, operation)'
                    'VALUES (%s, %s, %s, %s, %s) RETURNING id',
                    (method, status_code, request_body, response_body, 'Fibbonaci')
                )
                result = cur.fetchone()
                if not result:
                    print("No ID returned from INSERT")
                    return None

                request_id = result[0]
                conn.commit()
                print(f"Successfully saved fibbonaci request: {request_id}")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Database error in Fibbonaci.save(): {e.pgerror}")
            print(f"Database error code: {e.pgcode}")
            return None
