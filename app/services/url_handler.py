import httpx
from bs4 import BeautifulSoup
from app.settings import TIMEOUT, USER_AGENT

def fetch_url_content(url):
    """Загружает содержимое страницы и извлекает title с обработкой перенаправлений (максимум 3 перехода)."""
    headers = {"User-Agent": USER_AGENT}
    max_redirects = 3
    redirect_count = 0

    while redirect_count <= max_redirects:
        try:
            response = httpx.get(url, headers=headers, timeout=TIMEOUT, follow_redirects=False)
            
            # Проверяем, является ли статус код перенаправлением
            if response.status_code in (301, 302, 303, 307, 308):
                if 'Location' in response.headers:
                    url = response.headers['Location']
                    redirect_count += 1
                    print(f"Перенаправление на: {url} (переход {redirect_count})")
                    continue
                else:
                    print(f"Перенаправление без заголовка Location для URL: {url}")
                    return "Ошибка: отсутствует заголовок Location при перенаправлении"
            
            # Если статус код успешный, извлекаем заголовок
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "Без заголовка"
            return title.strip()
        
        except httpx.HTTPError as http_err:
            print(f"HTTP ошибка при обработке URL {url}: {http_err}")
            return "Ошибка HTTP"
        except Exception as e:
            print(f"Ошибка при обработке URL {url}: {e}")
            return "Ошибка"

    print(f"Превышен лимит перенаправлений ({max_redirects}) для URL: {url}")
    return "Ошибка: слишком много перенаправлений"
