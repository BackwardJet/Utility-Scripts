import sys
import PyPDF2

fileName = sys.argv[1]


def run():
	if fileName[-4:] != '.pdf':
		print('Error: Not a pdf file')
	else: 
		pdfFileObj = open(fileName, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		pageNumString = "The number of pages in the file is: " + str(pdfReader.numPages)
		print(pageNumString)

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
		
		print('Blank pages have been added to your file!')
		print('You will find the modified version of your file at ' + outputFileName)


if __name__ == '__main__':
	run()
