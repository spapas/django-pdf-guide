import sys
from PyPDF2 import PdfFileMerger


if __name__ == '__main__':
    pdfs = sys.argv[1:]

    if not pdfs or len(pdfs) < 2:
        exit("Please enter at least two pdfs for merging!")

    merger = PdfFileMerger()
    
    for pdf in pdfs:
        merger.append(fileobj=open(pdf, "rb"))
        
    output = open("output.pdf", "wb")
    merger.write(output)
    