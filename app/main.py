import sys
from app.services.url_handler import fetch_url_content
from app.services.file_handler import read_input_files, save_to_csv
from app.services.categorizer import classify_content
from app.settings import API_KEY

def main():
    if len(sys.argv) < 3:
        print("Использование: python main.py <путь_к_URL_файлу> <путь_к_категориям_файлу>")
        sys.exit(1)

    url_file = sys.argv[1]
    categories_file = sys.argv[2]

    print("Чтение входных данных...")
    urls, categories = read_input_files(url_file, categories_file)

    results = []

    print("Обработка URL...")
    for url in urls:
        print(f"Обрабатывается: {url}")
        title = fetch_url_content(url)
        category = classify_content(title, categories, API_KEY)
        results.append((url, category, title))

    print("Сохранение результатов...")
    save_to_csv(results, "output/result.csv")

    print("Обработка завершена. Результаты сохранены в output/result.csv")

if __name__ == "__main__":
    main()