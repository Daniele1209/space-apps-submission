import pdfplumber
import string
import os
import re


def normalize(text):
    # lower case normalization
    text = text.lower()
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # remove special chars and numbers (if you want to remove newlines also, delete '\n' from the regex)
    text = re.sub(r'[^A-Za-z \n]+', '', text)
    # remove extra whitespaces
    text = re.sub(' +', ' ', text)
    # remove empty lines
    text = "".join([s for s in text.strip().splitlines(True) if s.strip("\r\n").strip()])
    # remove leading whitespaces
    text = re.sub(r"^ +", "", text)
    return text


entries = os.listdir('Data/Corpus')

for file in entries:
    with pdfplumber.open('Data/Corpus/' + file) as pdf:
        filename = file.replace('pdf', 'txt')
        for page in pdf.pages:
            # Normalization:
            norm_page = normalize(page.extract_text())
            with open('Data/TextFiles/' + filename, 'a') as f:
                f.write(norm_page)