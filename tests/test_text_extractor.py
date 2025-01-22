import pytest
from app.services.text_extractor import extract_text_blocks

def test_extract_text_blocks_success():
    html_content = """
    <html>
        <h1>Header</h1>
        <p>Paragraph 1</p>
        <p>Paragraph 2</p>
    </html>
    """
    result = extract_text_blocks(html_content)
    assert result == "Header\nParagraph 1\nParagraph 2"

def test_extract_text_blocks_empty():
    html_content = "<html></html>"
    result = extract_text_blocks(html_content)
    assert result == ""

def test_extract_text_blocks_invalid_html():
    html_content = "<html><div>Missing tags"
    result = extract_text_blocks(html_content)
    assert result == ""