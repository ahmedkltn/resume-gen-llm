from fastapi.responses import FileResponse
from app.services.latex_generator import render_latex_to_pdf
import os
from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser import extract_text_from_file
from app.services.utils import clean_resume_text
from app.langchain_logic.chains import generate_tailored_resume
from starlette.background import BackgroundTask

router = APIRouter()

@router.post("/")
async def generate_resume(resume: UploadFile = File(...), job_description: str = Form()):
    resume_text_raw = await extract_text_from_file(resume)
    resume_text_cleaned = clean_resume_text(resume_text_raw)

    latex_resume = generate_tailored_resume(resume_text_cleaned, job_description)
    pdf_path = render_latex_to_pdf("resume_template.tex",latex_resume)

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"{resume.filename}_tailored.pdf",
        background=BackgroundTask(os.remove, pdf_path)
    )
