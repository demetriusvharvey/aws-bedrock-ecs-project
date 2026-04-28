from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import os

app = FastAPI()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "amazon.nova-micro-v1:0")

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def health_check():
    return {"status": "ok", "service": "bedrock-api"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        response = bedrock_runtime.converse(
            modelId=BEDROCK_MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": req.prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": 256,
                "temperature": 0.7,
                "topP": 0.9
            }
        )

        output_message = response["output"]["message"]["content"][0]["text"]

        return {
            "model_id": BEDROCK_MODEL_ID,
            "response": output_message
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))