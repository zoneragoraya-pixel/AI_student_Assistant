import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_answer(query):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    models = [
        "llama-3.1-8b-instant",
        "llama-3.1-70b-versatile",
        "gemma2-9b-it"
    ]

    for model in models:
        try:
            print(f"Trying model: {model}")

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": query}
                ]
            )

            answer = response.choices[0].message.content
            return answer, model

        except Exception as e:
            print(f"Model {model} failed: {e}")

    return "AI failed on all models. Check API key or internet.", "error"