from typing import List

from .IngestorInterface import IngestorInterface, QuoteModel 
from .DocxImporter import DocxImporter
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFImporter, PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    importers = [DocxImporter, CSVImporter, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel.QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)