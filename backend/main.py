
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise Exception("GROQ_API_KEY not found in .env file")

# Create FastAPI app (THIS is what uvicorn looks for)
app = FastAPI()

# Create Groq OpenAI-compatible client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

# Request body model
class ChatRequest(BaseModel):
    message: str


def ask_ai(prompt):
    response = client.responses.create(
        input=prompt,
        model="openai/gpt-oss-20b"
    )
    return response.output_text


@app.post("/chat")
def chat(req: ChatRequest):
    try:
        reply = ask_ai(req.message)
        return {"response": reply}
    except Exception as e:
        return {"error": str(e)}
