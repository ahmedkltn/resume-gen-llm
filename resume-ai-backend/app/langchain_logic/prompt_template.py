from langchain.prompts import PromptTemplate

resume_prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template="""
You are an expert resume optimizer with deep knowledge of ATS systems and hiring practices.

CRITICAL INSTRUCTIONS:
- NEVER add skills, experiences, or qualifications that don't exist in the original resume
- ONLY reorganize, rephrase, and emphasize existing content
- Use keywords from the job description where they naturally align with existing experience
- Maintain factual accuracy - do not exaggerate or fabricate anything

ORIGINAL RESUME:
{resume}

JOB DESCRIPTION:
{job}

TASK: Optimize the resume by:
1. Reordering sections to highlight most relevant experience first
2. Rephrasing existing bullet points to better match job requirements using industry keywords
3. Emphasizing skills and experiences that align with the job description
4. Ensuring ATS compatibility with clear formatting and relevant keywords
5. Maintaining the same overall structure and length

FORMATTING REQUIREMENTS:
- Keep the same sections (Experience, Skills, Education, etc.)
- Use action verbs and quantifiable achievements where they already exist
- Ensure consistency in tense and style
- Include relevant keywords naturally within existing content

OUTPUT REQUIREMENTS:
- Return ONLY the LaTeX body content (no \\documentclass, \\begin{{document}}, or \\end{{document}})
- Use proper LaTeX formatting with double curly braces for LaTeX commands
- Use sections like \\section*{{Experience}}, \\section*{{Skills}}, \\section*{{Education}}
- Ensure all LaTeX syntax uses double curly braces: \\textbf{{text}}, \\textit{{text}}, \\item, etc.
- Include proper line breaks with \\\\ where needed
- Use \\begin{{itemize}} and \\end{{itemize}} for bullet points
- Start directly with the resume content - no explanations or additional text

EXAMPLE LATEX STRUCTURE:
\\begin{{center}}
\\textbf{{\\Large CANDIDATE NAME}} \\\\
Email: email@example.com $\\mid$ Phone: (555) 123-4567 \\\\
\\end{{center}}

\\section*{{EXPERIENCE}}
\\textbf{{Job Title}} \\hfill \\textit{{Date Range}} \\\\
\\textit{{Company Name}} \\\\
\\begin{{itemize}}
\\item Achievement or responsibility
\\end{{itemize}}
"""
)

cover_prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template="""
Create a professional cover letter based on the resume and job description provided.

IMPORTANT INSTRUCTIONS:
1. Extract the candidate's name, contact information, and experience from the resume
2. Do NOT include placeholders like [Your Name], [Your Address], or [Date]
3. Do NOT mention where the job was found or use "Dear Hiring Manager"
4. Start directly with the company name if mentioned in the job description
5. Focus on specific achievements and quantifiable results from the resume
6. Keep it concise (3-4 paragraphs maximum)
7. End with a professional closing using the candidate's actual name

Resume:
{resume}

Job Description:
{job}

OUTPUT REQUIREMENTS:
- Return ONLY the LaTeX body content (no \\documentclass, \\begin{{document}}, or \\end{{document}})
- Use proper LaTeX formatting with double curly braces for LaTeX commands
- Use standard business letter formatting
- Ensure all LaTeX syntax uses double curly braces: \\textbf{{text}}, \\textit{{text}}, etc.
- Include proper line breaks with \\\\ where needed
- Start directly with the cover letter content - no explanations or additional text

EXAMPLE LATEX STRUCTURE:
\\begin{{flushleft}}
Candidate Name \\\\
Email Address \\\\
Phone Number \\\\
\\end{{flushleft}}

\\vspace{{0.5cm}}

\\begin{{flushleft}}
Company Name \\\\
Department (if known) \\\\
\\end{{flushleft}}

\\vspace{{0.5cm}}

Dear Hiring Team,

Paragraph content goes here...

\\vspace{{0.3cm}}

Sincerely,

\\vspace{{0.3cm}}

Candidate Name
"""
)