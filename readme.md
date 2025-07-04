
# Resume & Cover Letter Generator (LLM-Powered)

This project allows you to generate tailored resumes and cover letters using an AI model (Gemini 1.5 Pro). Built with:

- ⚡ Next.js (Frontend)
- 🐍 FastAPI (Backend)
- 🤖 LangChain + Gemini API
- 📄 PDF generation via LaTeX

---

## 📦 Requirements

- Docker
- Docker Compose

---

## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/resume-ai.git
   cd resume-ai
   ```

2. Build and run the services:

   ```bash
   docker-compose up -d
   ```

3. Access the app:

   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:8080](http://localhost:8080)

---

## 📁 Structure

```bash
resume-ai/
├── resume-ai-frontend/   # Next.js frontend
├── resume-ai-backend/    # FastAPI backend
└── docker-compose.yml
```

---

## 📌 Notes

- Ensure your `Gemini` API key is set properly in the backend `.env`.
- Frontend uploads a PDF resume and job description, and receives downloadable PDF files for the resume and cover letter.

---
