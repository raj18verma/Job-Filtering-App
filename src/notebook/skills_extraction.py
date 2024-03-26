import spacy
from spacy.matcher import Matcher
import PyPDF2
import os

# Load the Spacy English model
nlp = spacy.load(r'c:\users\rajve\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages\en_core_web_sm\en_core_web_sm-3.7.1')

import csv
from spacy.matcher import Matcher
import csv

# Read skills from CSV file
file_path=r'D:\UNSTOP\Job-Filtering-App\src\notebook\skills.csv'
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    skills = [row for row in csv_reader]

# Create pattern dictionaries from skills
skill_patterns = [[{'LOWER': skill}] for skill in skills[0]]

# Create a Matcher object
matcher = Matcher(nlp.vocab)

# Add skill patterns to the matcher
for pattern in skill_patterns:
    matcher.add('Skills', [pattern])

# Function to extract skills from text
def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)
    skills = set()
    for match_id, start, end in matches:
        skill = doc[start:end].text
        skills.add(skill)
    return skills

# Function to extract text from PDF
def extract_text_from_pdf(file_path:str):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def skills_extractor(file_path):
        # Extract text from PDF
        path=r'D:\UNSTOP\Job-Filtering-App\src\notebook'
        full_file_path = os.path.join(path, file_path)
        resume_text = extract_text_from_pdf(full_file_path)

        # Extract skills from resume text
        skills = list(extract_skills(resume_text))
        return skills


