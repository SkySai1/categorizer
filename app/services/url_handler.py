import httpx
from bs4 import BeautifulSoup
from app.settings import TIMEOUT, USER_AGENT

def fetch_url_content(url):
    """Загружает содержимое страницы и извлекает title."""
    headers = {"User-Agent": USER_AGENT}
    try:
        response = httpx.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Без заголовка"
        return title.strip()
    except Exception as e:
        print(f"Ошибка при обработке URL {url}: {e}")
        return "Ошибка"