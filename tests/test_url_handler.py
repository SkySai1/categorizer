import pytest
from unittest.mock import patch
from app.services.url_handler import fetch_url_content

@patch("app.services.url_handler.httpx.get")
def test_fetch_url_content_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "<html><title>Test Title</title></html>"

    result = fetch_url_content("https://example.com")
    assert result == "Test Title"

@patch("app.services.url_handler.httpx.get")
def test_fetch_url_content_no_title(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "<html></html>"

    result = fetch_url_content("https://example.com")
    assert result == "Без заголовка"

@patch("app.services.url_handler.httpx.get")
def test_fetch_url_content_error(mock_get):
    mock_get.side_effect = Exception("Connection Error")

    result = fetch_url_content("https://example.com")
    assert result == "Ошибка"