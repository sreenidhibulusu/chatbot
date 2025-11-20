import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

def generate_response(prompt):
    model = "gpt-3.5-turbo"
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=256
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI API error: {e}]"