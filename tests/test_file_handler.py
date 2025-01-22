import pytest
import os
from app.services.file_handler import read_input_files, save_to_csv

def test_read_input_files(tmp_path):
    url_file = tmp_path / "urls.txt"
    categories_file = tmp_path / "categories.txt"

    url_file.write_text("https://example.com\nhttps://test.com")
    categories_file.write_text("Category A\nCategory B")

    urls, categories = read_input_files(url_file, categories_file)

    assert urls == ["https://example.com", "https://test.com"]
    assert categories == ["Category A", "Category B"]

def test_save_to_csv(tmp_path):
    output_file = tmp_path / "result.csv"
    data = [
        ("https://example.com", "Category A", "Example Title"),
        ("https://test.com", "Category B", "Test Title")
    ]

    save_to_csv(data, output_file)

    assert output_file.exists()
    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert lines[1].strip() == "https://example.com,Category A,Example Title"
        assert lines[2].strip() == "https://test.com,Category B,Test Title"