from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from core.config import OPENAI_API_KEY

router = APIRouter()

client = OpenAI(api_key=OPENAI_API_KEY)


class ChatRequest(BaseModel):
    message: str


@router.post("/ai-chat")
def ai_chat(req: ChatRequest):
    try:
        if not req.message:
            raise HTTPException(status_code=400, detail="Message is required")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant for a Healthcare CRM system."
                },
                {
                    "role": "user",
                    "content": req.message
                }
            ]
        )

        return {
            "response": response.choices[0].message.content
        }

    except Exception as e:
        # 🔥 SAFE FALLBACK (IMPORTANT FIX)
        return {
            "response": f"[FALLBACK MODE] {req.message}",
            "error": str(e)
        }