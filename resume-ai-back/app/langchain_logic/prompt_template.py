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

OUTPUT: Return the optimized resume in LaTeX format using a clean and professional style. Use sections such as \section*[Experience], \section*[Skills], \section*[Education], and consistent formatting throughout. Do not include the full LaTeX document (no \documentclass or \begin[document]); return only the LaTeX body content that can be inserted into a resume template.
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
    
    OUTPUT: Return the cover letter in LaTeX format. Use a standard business letter layout with appropriate line breaks, indentation, and formatting. Do not include the full LaTeX document (no \documentclass or \begin[document]); return only the LaTeX body content that can be inserted into a resume template.
    """
)


update_resume = PromptTemplate(
    input_variables=["resume", "prompt"],
    template="""
You are a professional resume editor with expertise in customizing resumes based on specific user requirements.

CRITICAL RULES:
- NEVER add experiences, skills, or qualifications that don't exist in the original resume
- ONLY modify, reorganize, or rephrase existing content
- Maintain factual accuracy and truthfulness
- Follow the user's specific instructions precisely

CURRENT RESUME:
{resume}

USER INSTRUCTIONS:
{prompt}

TASK: Update the resume according to the user's specific requirements while maintaining:
1. All factual information from the original resume
2. Professional formatting and structure
3. Consistency in style and tone
4. Proper grammar and spelling

OUTPUT: Return the updated resume in LaTeX format using a clean and professional layout. Use standard sections such as \section*{Experience}, \section*{Skills}, \section*{Education}, and ensure consistent styling. Do not include a full LaTeX document setup.
"""
)

# User-directed cover letter update prompt
update_cover_letter = PromptTemplate(
    input_variables=["cover_letter", "prompt"],
    template="""
You are a professional cover letter editor specializing in customizing cover letters based on specific user feedback.

CURRENT COVER LETTER:
{cover_letter}

USER INSTRUCTIONS:
{prompt}

TASK: Update the cover letter according to the user's specific requirements while maintaining:
1. Professional business letter format
2. Appropriate tone and style
3. Logical flow and structure
4. Proper grammar and spelling
5. Relevance to the job opportunity

Common update requests you can handle:
- Adjusting tone (more formal/casual, confident/humble)
- Changing focus (different skills/experiences to highlight)
- Modifying length (shorter/longer)
- Restructuring paragraphs
- Updating specific phrases or sentences
- Changing the opening/closing

OUTPUT: Return the updated cover letter in LaTeX format. Maintain a professional business letter layout and proper formatting. Return only the body content without full LaTeX document structure.
"""
)
