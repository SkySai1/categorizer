# Настройки приложения
API_KEY = "your_openai_api_key_here"
PROMPT_TEMPLATE = (
    "На основании следующего текста выберите категорию из списка: {categories}.\n"
    "Текст:\n{content}"
)
TIMEOUT = 10  # Таймаут запросов в секундах
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"