from bs4 import BeautifulSoup

def extract_text_blocks(html_content):
    """Извлекает текстовые блоки из HTML-содержимого."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Извлекаем текст из стандартных тегов, таких как <p>, <h1>, <h2>, и т.д.
        text_blocks = []
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
            text = tag.get_text(strip=True)
            if text:
                text_blocks.append(text)
        return "\n".join(text_blocks)  # Объединяем блоки текста в одну строку
    except Exception as e:
        print(f"Ошибка извлечения текста: {e}")
        return ""