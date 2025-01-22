import pytest
from unittest.mock import patch
from app.main import main

@patch("app.main.fetch_url_content")
@patch("app.main.read_input_files")
@patch("app.main.save_to_csv")
@patch("app.main.classify_content")
def test_main(mock_classify, mock_save, mock_read, mock_fetch, tmp_path):
    mock_read.return_value = (["https://example.com"], ["Category A", "Category B"])
    mock_fetch.return_value = "Example Title"
    mock_classify.return_value = "Category A"

    output_file = tmp_path / "result.csv"

    mock_api_key = "org-M7Y1vaSgmrFCvGUXg084YXNu"  # Используем реальное значение для соответствия
    with patch("app.settings.OUTPUT_DIR", str(tmp_path)):
        with patch("app.settings.API_KEY", mock_api_key):
            main(["main.py", "test_urls.txt", "test_categories.txt"])

    mock_read.assert_called_once()
    mock_fetch.assert_called_once_with("https://example.com")
    mock_classify.assert_called_once_with("Example Title", ["Category A", "Category B"], mock_api_key)
    mock_save.assert_called_once()