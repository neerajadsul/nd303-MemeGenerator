import argparse
import random

from QuoteEngine import CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Provide input to Meme Creator')

   parser.add_argument('-body', type=str)
   parser.add_argument('-author', type=str)
   parser.add_argument('-path', type=str)

   

   base_path = '/Users/Neeraj/Development/meme_generator/_data/DogQuotes/'
    # print(CSVIngestor.parse(base_path + 'DogQuotesCSV.csv'))
    # print(DocxIngestor.parse(base_path + 'DogQuotesDOCX.docx'))
    # print(PDFIngestor.parse(base_path + 'DogQuotesPDF.pdf'))
    # print(TXTIngestor.parse(base_path + 'DogQuotesTXT.txt'))    
    # print(Ingestor.Ingestor.parse(base_path + 'DogQuotesCSV.csv'))

    meme_gen = MemeEngine('/Users/Neeraj/Development/meme_generator/_data')
    output = meme_gen.make_meme(
       '/Users/Neeraj/Development/meme_generator/_data/photos/dog/xander_1.jpg',
       'Hello World!',
       'Macbook Pro'
    )
    print(output)
    
