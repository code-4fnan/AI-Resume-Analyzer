import fitz

def extract_resume_text(pdf_file):
    text = ""

    document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()
