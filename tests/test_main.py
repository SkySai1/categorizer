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

    with patch("app.settings.OUTPUT_DIR", str(tmp_path)):
        main()

    mock_read.assert_called_once()
    mock_fetch.assert_called_once_with("https://example.com")
    mock_classify.assert_called_once_with("Example Title", ["Category A", "Category B"], "your_openai_api_key_here")
    mock_save.assert_called_once()