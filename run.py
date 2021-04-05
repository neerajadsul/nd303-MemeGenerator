from QuoteEngine import CSVIngestor, DocxIngestor, PDFIngestor
if __name__ == '__main__':
    # print(CSVIngestor.parse('/Users/Neeraj/Development/meme_generator/_data/DogQuotes/DogQuotesCSV.csv'))
    # print(DocxIngestor.parse('/Users/Neeraj/Development/meme_generator/_data/DogQuotes/DogQuotesDOCX.docx'))
    print(PDFIngestor.parse('/Users/Neeraj/Development/meme_generator/_data/DogQuotes/DogQuotesPDF.pdf'))

