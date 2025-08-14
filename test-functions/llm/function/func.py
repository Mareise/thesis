# Function
import logging
import json
import torch
import time
from transformers import pipeline


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.bfloat16,
    device_map="auto" if torch.cuda.is_available() else None
)


def new():
    return Function()


class Function:
    async def handle(self, scope, receive, send):
        try:
            # Read request body
            body = b""
            more_body = True
            while more_body:
                message = await receive()
                if message["type"] == "http.request":
                    body += message.get("body", b"")
                    more_body = message.get("more_body", False)

            data = json.loads(body.decode())

            input = data.get("prompt", None)
            if not input:
                raise ValueError("Missing 'prompt'")

            messages = [{"role": "user", "content": input},
]

            # Run inference and measure time
            start = time.perf_counter()
            prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
            duration = time.perf_counter() - start

            await send({
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"application/json"]],
            })
            await send({
                "type": "http.response.body",
                "body": json.dumps({
                    "output": outputs[0]["generated_text"],
                    "device": str(device),
                    "inference_time_sec": round(duration, 2)
                }).encode("utf-8")
            })

        except Exception as e:
            logging.exception("LLM Error")
            await send({
                "type": "http.response.start",
                "status": 400,
                "headers": [[b"content-type", b"application/json"]],
            })
            await send({
                "type": "http.response.body",
                "body": json.dumps({"error": str(e)}).encode("utf-8")
            })
