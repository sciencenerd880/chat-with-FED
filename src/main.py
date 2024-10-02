'''
from utils.openai_helper import translate_prompt

response = translate_prompt(prompt = "what is the FED's favourite line?"
                            )

print(response)
'''

# src/main.py

from fastapi import FastAPI
from src.api.translate import router as translate_router

# Create the FastAPI app
app = FastAPI()

# Include the translation router
app.include_router(translate_router)

# Optional root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the GPT-4 translation service!"}
