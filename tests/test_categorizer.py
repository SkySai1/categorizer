import pytest
from unittest.mock import patch
from app.services.categorizer import classify_content

@patch("openai.ChatCompletion.create")
@patch("app.settings.API_KEY", "your_openai_api_key_here")  # Подмена API_KEY
def test_classify_content_success(mock_openai):
    mock_openai.return_value = {
        'choices': [
            {'message': {'content': 'Category A'}}
        ]
    }

    result = classify_content("Sample text", ["Category A", "Category B"], "your_openai_api_key_here")
    assert result == "Category A"

@patch("openai.ChatCompletion.create")
@patch("app.settings.API_KEY", "your_openai_api_key_here")  # Подмена API_KEY
def test_classify_content_error(mock_openai):
    mock_openai.side_effect = Exception("API Error")

    result = classify_content("Sample text", ["Category A", "Category B"], "your_openai_api_key_here")
    assert result == "Не удалось классифицировать"