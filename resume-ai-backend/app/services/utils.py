import re

def clean_resume_text(text: str) -> str:
    # Remove extra whitespace and empty lines
    text = re.sub(r'\n\s*\n+', '\n', text)           # Collapse multiple empty lines
    text = re.sub(r'[ \t]+', ' ', text)              # Replace tabs/multiple spaces with single space
    text = re.sub(r'\n{3,}', '\n\n', text)           # Avoid more than 2 consecutive newlines
    text = text.strip()
    return text