import PyPDF2

fileName = 'syllabus.pdf'#sys.argv[1]

pdfFileObj = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)	
	pdfWriter.addPage(pageObj)
	pdfWriter.addBlankPage()

outputFileName = fileName[:-4]+'-pages-added.pdf'
pdfOutputFile = open(outputFileName, 'wb')

pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

pdfFileObj.close()
