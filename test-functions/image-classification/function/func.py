# Function
import logging
from torchvision import models, transforms
import json
import torch
import base64
from PIL import Image
import io

model = models.resnet18(pretrained=True)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# do i ned to do this?
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])


def new():
    """ New is the only method that must be implemented by a Function.
    The instance returned can be of any name.
    """
    return Function()


class Function:
    async def handle(self, scope, receive, send):
        logging.info("OK: Request Received")

        try:
            # Wait for the request body
            body = b""
            more_body = True
            while more_body:
                message = await receive()
                if message["type"] == "http.request":
                    body += message.get("body", b"")
                    more_body = message.get("more_body", False)

            data = json.loads(body.decode())

            if "image_base64" not in data:
                raise ValueError("Missing 'image_base64' in request.")

            # Decode image
            image_data = base64.b64decode(data["image_base64"])
            image = Image.open(io.BytesIO(image_data)).convert("RGB")
            input_tensor = preprocess(image).unsqueeze(0).to(device)

            # Run inference
            with torch.no_grad():
                output = model(input_tensor)
                pred = torch.argmax(output, dim=1).item()

            print(f"Predicted class index: {pred}")

            await send({
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"application/json"],
                ],
            })
            await send({
                'type': 'http.response.body',
                'body': json.dumps({
                        "class_index": pred,
                        "device": str(device),
                    }).encode('utf-8')
            })

        except Exception as e:
            logging.exception("Error processing request")
            error_message = json.dumps({"error": str(e)}).encode("utf-8")
            await send({
                "type": "http.response.start",
                "status": 400,
                "headers": [
                    [b"content-type", b"application/json"],
                ],
            })
            await send({
                "type": "http.response.body",
                "body": error_message,
            })
