import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

openai = OpenAI(api_key=api_key)

SYSTEM_PROMPT = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring navigation text. "
    "Respond in markdown."
)

def message(website):
    return[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":f"Website title: {website.title}\n\n{website.text}"}
    ]

def get_summary(website):
    messages = message(website)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content