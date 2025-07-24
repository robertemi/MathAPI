from models.Factorial import Factorial
from models.Fibbonaci import Fibbonaci
from models.Power import Power

class MathController:
    def __init__(self, db_connection):
        self.operations = {
            "factorial": Factorial(),
            "fibbonaci": Fibbonaci(),
            "power": Power()
        }
        self.db_connection = db_connection

    def handle_request(self, operation: str, **inputs):
        try:
            operator = self.operations[operation.lower()]

            if operation == 'factorial':
                result = operator.compute(inputs['number'])
            elif operation == "fibbonaci":
                result = operator.compute(inputs['number'])
            elif operation == "power":
                result = operator.compute(inputs['number'], inputs['power'])
            else:
                raise ValueError(f"Unsupported operation: {operation}")
            
            # persist API call to DB
            operator.save(
                conn=self.db_connection,
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

        
    
