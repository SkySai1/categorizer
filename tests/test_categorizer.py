import pytest
from unittest.mock import patch
from app.services.categorizer import classify_content

@patch("app.services.categorizer.openai.ChatCompletion.create")
def test_classify_content_success(mock_openai):
    mock_openai.return_value = {
        'choices': [
            {'message': {'content': 'Category A'}}
        ]
    }

    result = classify_content("Sample text", ["Category A", "Category B"], "fake_api_key")
    assert result == "Category A"

@patch("app.services.categorizer.openai.ChatCompletion.create")
def test_classify_content_error(mock_openai):
    mock_openai.side_effect = Exception("API Error")

    result = classify_content("Sample text", ["Category A", "Category B"], "fake_api_key")
    assert result == "Не удалось классифицировать"