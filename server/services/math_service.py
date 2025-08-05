from utils import operations as op
import json


class MathService:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    async def _save_to_db(
            self,
            conn,
            method,
            status_code,
            request_body,
            response_body,
            operation
    ):

        try:
            await conn.fetchrow(
                """INSERT INTO api_requests (
                                            method,
                                            status_code,
                                            request_body,
                                            response_body,
                                            operation
                                            )
                   VALUES ($1, $2, $3, $4, $5)""",
                method,
                status_code,
                json.dumps(request_body),
                json.dumps(response_body),
                operation
            )
        except Exception as e:
            print(f"DB logging error: {e}")

    async def compute(self, conn, operation, **inputs):
        redis = await self.redis_client()
        cache_key = f"{operation}:{inputs}"

        cached = await redis.get(cache_key)

        if cached:
            return json.loads(cached)

        if operation == "factorial":
            result = op.factorial(inputs["number"])
        elif operation == "fibbonaci":
            result = op.fibbonaci(inputs["number"])
        elif operation == "power":
            result = op.power(inputs["base"], inputs["exponent"])
        else:
            raise ValueError("Unsupported operation")

        await redis.setex(cache_key, 1800, json.dumps(result))

        await self._save_to_db(
            conn,
            "POST",
            200,
            inputs,
            {"result": result},
            operation
        )

        return result
