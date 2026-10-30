import re

SKILLS = [
    "Python", "Java", "C++", "SQL", "HTML", "CSS", "JavaScript",
    "React", "Angular", "Spring Boot", "Django", "Flask",
    "Machine Learning", "Deep Learning", "NLP", "TensorFlow",
    "PyTorch", "AWS", "Azure", "Docker", "Kubernetes",
    "Power BI", "Excel", "Pandas", "NumPy", "MongoDB",
    "MySQL", "Git", "REST API", "Data Analysis"
]

def extract_skills(text):
    found = []

    for skill in SKILLS:
        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'
        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found
