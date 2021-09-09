"""Aggregates the four specific file type ingestors. Will parse a
file provided in the class method parse, and return a list of
 QuoteModel objects."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .TXTIngestor import TXTIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    ingestors = [TXTIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
