import fitz

def extract_text(file):
    doc = fitz.open(stream=file.file.read(), filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text()

    return text