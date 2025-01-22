import openai
from app.settings import PROMPT_TEMPLATE

def classify_content(content, categories, api_key):
    """Классифицирует текст с использованием OpenAI GPT."""
    try:
        openai.api_key = api_key  # Установка ключа API
        prompt = PROMPT_TEMPLATE.format(categories=", ".join(categories), content=content)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Ошибка классификации текста: {e}")
        return "Не удалось классифицировать"