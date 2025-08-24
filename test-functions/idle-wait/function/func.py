# Function
import logging
import time
import json

def new():
    return Function()


class Function:
    async def handle(self, scope, receive, send):
        logging.info("OK: Request Received")
        # Read the request body
        body = b""
        more_body = True
        while more_body:
            message = await receive()
            body += message.get("body", b"")
            more_body = message.get("more_body", False)

        try:
            payload = json.loads(body.decode())
        except Exception:
            payload = {}


        wait_time = int(payload.get("wait_time", 2))
        time.sleep(wait_time)

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': 'OK'.encode(),
        })