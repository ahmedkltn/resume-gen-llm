import io
import docx
import fitz  # PyMuPDF
from fastapi import UploadFile

async def extract_text_from_file(file: UploadFile) -> str:
    content = await file.read()

    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=content, filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
        doc.close()
        return text

    elif file.filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(content))
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    else:
        return content.decode("utf-8")  # fallback: plain text
