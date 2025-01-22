from openai import OpenAI
import os
from app.settings import PROMPT_TEMPLATE, PROXY_ADDRESS, PROXY_PORT

def classify_content(content, categories, api_key):
    """Классифицирует текст с использованием OpenAI GPT через прокси."""
    try:
        # Проверка наличия и непустоты переменных прокси
        if PROXY_ADDRESS and PROXY_PORT:
            # Установка переменных окружения для прокси
            os.environ["HTTP_PROXY"] = f"http://{PROXY_ADDRESS}:{PROXY_PORT}"
            os.environ["HTTPS_PROXY"] = f"http://{PROXY_ADDRESS}:{PROXY_PORT}"
            print("Прокси-сервер установлен:", PROXY_ADDRESS, PROXY_PORT)
        else:
            print("Прокси-сервер не задан или неполный. Используется прямое соединение.")

        # Создание клиента OpenAI с ключом API и прокси
        client = OpenAI(api_key=api_key)
        
        # Формирование запроса
        prompt = PROMPT_TEMPLATE.format(categories=", ".join(categories), content=content)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Возврат результата
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Ошибка классификации текста: {e}")
        return "Не удалось классифицировать"
