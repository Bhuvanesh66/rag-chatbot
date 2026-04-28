import requests
import os
from dotenv import load_dotenv

def generate_answer(context, query, chat_history):
    load_dotenv()
    api_key = os.getenv("GITHUB_TOKEN")

    url = "https://models.inference.ai.azure.com/chat/completions"

    history_text = "\n".join(
        [f"Q: {q}\nA: {a}" for q, a in chat_history[-3:]]
    )

    prompt = f"""
You are a STRICT multilingual PDF-grounded assistant.

RULES:
1. Answer ONLY from the provided context
2. ALWAYS include citations like (Page X)
3. If answer is not in the context → say:
   "Not found in document"
4. DO NOT hallucinate

MULTILINGUAL RULES:
5. Detect the language of the question
6. Answer in the SAME language as the question
7. Keep citations EXACTLY in format: (Page X)
8. Do NOT translate citations

Conversation History:
{history_text}

Context:
{context}

Question:
{query}
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError(response.text)

    return response.json()["choices"][0]["message"]["content"]