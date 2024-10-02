# src/api/translate.py

from fastapi import APIRouter
from pydantic import BaseModel
from src.utils.openai_helper import translate_prompt

# Create a router object for FastAPI
router = APIRouter()

# Define the request model (expecting a "prompt" field)
class TranslationRequest(BaseModel):
    prompt: str

# Define the translation endpoint
@router.post("/translate")
async def translate(request: TranslationRequest):
    # Use the OpenAI helper function to perform translation
    translation = translate_prompt(request.prompt)
    return {"translation": translation}
