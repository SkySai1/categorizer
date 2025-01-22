import os
import pandas as pd

def read_input_files(url_file_path, categories_file_path):
    """Читает входные файлы со списком URL и категорий."""
    try:
        with open(url_file_path, 'r', encoding='utf-8') as url_file:
            urls = [line.strip() for line in url_file if line.strip()]

        with open(categories_file_path, 'r', encoding='utf-8') as categories_file:
            categories = [line.strip() for line in categories_file if line.strip()]

        return urls, categories
    except Exception as e:
        print(f"Ошибка чтения входных файлов: {e}")
        return [], []

def save_to_csv(data, output_file_path):
    """Сохраняет данные в CSV-файл."""
    try:
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        df = pd.DataFrame(data, columns=["URL", "Category", "Title"])
        df.to_csv(output_file_path, index=False, encoding='utf-8')
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")