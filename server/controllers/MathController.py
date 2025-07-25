from models.Factorial import Factorial
from models.Fibbonaci import Fibbonaci
from models.Power import Power
from models.User import User

class MathController:
    def __init__(self, redis_client):
        self.operations = {
            "factorial": Factorial(),
            "fibbonaci": Fibbonaci(),
            "power": Power()
        }
        self.redis_client = redis_client

    def handle_request(self, db_connection, operation: str, **inputs):
        try:
            operator = self.operations[operation.lower()]
            cache_key = f'{operation}:{inputs}'

            #check redis cache
            cached_result = self.redis_client.get(cache_key)
            if cached_result:
                return float(cached_result) if '.' in cached_result else int(cached_result) 

            #if not cached -> compute
            if operation == 'factorial':
                result = operator.compute(inputs['number'])
            elif operation == "fibbonaci":
                result = operator.compute(inputs['number'])
            elif operation == "power":
                result = operator.compute(inputs['number'], inputs['power'])
            else:
                raise ValueError(f"Unsupported operation: {operation}")
            
            #save computed result to redis for 30 minutes
            self.redis_client.setex(cache_key, 1800, result)
            
            # persist API call to DB
            operator.save(
                conn=db_connection,
                method='POST',
                status_code=200,
                request_body=inputs,
                response_body={"result": result}
            )
            return result

        except Exception as e:
            if hasattr(operator, 'save'):
                operator.save(
                    conn=self.db_conn,
                    method="POST",
                    status_code=400,
                    request_body=inputs,
                    response_body={"error": str(e)}
                )
            raise
    


        
    
