from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask
from app.services.parser import extract_text_from_file
from app.services.utils import clean_resume_text
from app.langchain_logic.chains import generate_tailored_cover_lettre
from app.services.latex_generator import render_latex_to_pdf
import os

router = APIRouter()

@router.post("/")
async def generate_cover_letter(resume: UploadFile = File(...), job_description: str = Form()):
    resume_text_raw = await extract_text_from_file(resume)
    resume_text_cleaned = clean_resume_text(resume_text_raw)

    latex_cover_letter = generate_tailored_cover_lettre(resume_text_cleaned, job_description)
    pdf_path = render_latex_to_pdf("cover_template.tex",latex_cover_letter)

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="tailored_cover_letter.pdf",
        background=BackgroundTask(os.remove, pdf_path)
    )