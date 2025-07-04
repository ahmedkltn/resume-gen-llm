import subprocess
import os
import uuid

def render_latex_to_pdf(template_path: str, body_content: str) -> str:
    # Load LaTeX template from file
    with open(template_path, "r") as file:
        template = file.read()

    # Generate a unique filename
    job_id = str(uuid.uuid4())[:8]
    tex_file = f"{job_id}.tex"
    pdf_file = f"{job_id}.pdf"

    # Insert body_content into the template
    latex_content = template.replace("{{ body }}", body_content)

    with open(tex_file, "w") as f:
        f.write(latex_content)

    # Compile LaTeX to PDF
    subprocess.run(["pdflatex", tex_file], check=True)

    # Clean up intermediate files
    for ext in ["aux", "log", "tex"]:
        try:
            os.remove(f"{job_id}.{ext}")
        except FileNotFoundError:
            pass

    return pdf_file