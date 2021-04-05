from QuoteEngine import CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor
from QuoteEngine import Ingestor
if __name__ == '__main__':
    base_path = '/Users/Neeraj/Development/meme_generator/_data/DogQuotes/'
    print(CSVIngestor.parse(base_path + 'DogQuotesCSV.csv'))
    print(DocxIngestor.parse(base_path + 'DogQuotesDOCX.docx'))
    print(PDFIngestor.parse(base_path + 'DogQuotesPDF.pdf'))
    print(TXTIngestor.parse(base_path + 'DogQuotesTXT.txt'))    
    print(Ingestor.Ingestor.parse(base_path + 'DogQuotesCSV.csv'))
