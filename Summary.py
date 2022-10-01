import PyPDF2
import os
entries = os.listdir('D:/Programming/space-apps-submission/Corpus')

#pdfFileObj = open('D:/Programming/space-apps-submission/Corpus/19900018794.pdf' , 'rb')
#print(entries)

for file in entries:
    try:
                # creating a pdf file object
                pdfFileObj = open(('D:/Programming/space-apps-submission/Corpus/' + file), 'rb')

                # creating a pdf reader object
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                # printing number of pages in pdf file
                print(pdfReader.numPages)

                # creating a page object
                pageObj = pdfReader.getPage(0)

                # extracting text from page
                print(pageObj.extractText())

                # closing the pdf file object
                pdfFileObj.close()

    break