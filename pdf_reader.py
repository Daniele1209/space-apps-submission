import pdfplumber
import string


def normalize(text):
    # lower case normalization
    text = text.lower()
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    print(text)
    return text


file = '19900018794.pdf'

with pdfplumber.open('Corpus/' + file) as pdf:
    for page in pdf.pages:
        # print(page.extract_text())
        # Normalization:
        norm_text = normalize(page.extract_text())

