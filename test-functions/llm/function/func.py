# Function
import logging
import json
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM


model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16, # if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else None,
)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

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

            prompt = data.get("prompt", None)
            if not prompt:
                raise ValueError("Missing 'prompt'")

            # Tokenize input
            inputs = tokenizer(prompt, return_tensors="pt").to(device)

            # Run inference and measure time
            start = time.perf_counter()
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=100,
                    do_sample=True,
                    temperature=0.7,
                )
            duration = time.perf_counter() - start

            response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            await send({
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"application/json"]],
            })
            await send({
                "type": "http.response.body",
                "body": json.dumps({
                    "output": response_text,
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
