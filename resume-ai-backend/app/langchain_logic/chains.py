from app.langchain_logic.llm_config import llm
from app.langchain_logic.prompt_template import resume_prompt, cover_prompt
from langchain.schema.output_parser import StrOutputParser

def generate_tailored_resume(resume_text: str, job_text: str) -> str:
    chain = resume_prompt | llm | StrOutputParser()
    result = chain.invoke({
        "resume": resume_text,
        "job": job_text
    })
    return result

def generate_tailored_cover_lettre(resume_text: str, job_text: str) -> str:
    chain = cover_prompt | llm | StrOutputParser()
    result = chain.invoke({
        "resume": resume_text,
        "job": job_text
    })
    return result