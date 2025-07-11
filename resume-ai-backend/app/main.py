from fastapi import FastAPI
from app.api import resume, cover
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(resume.router, prefix="/api/resume")
app.include_router(cover.router, prefix="/api/cover")
