"""Opens and ingests the contects of a docx file containing quotes

DocxInvestor realizes the IngestorInterface abstract class.

The class variable allowed_extensions adds docx to the list of allowed
extensions.

The class can run the IngestorInterface class method can_ingest to
confirm the file is a docx.

The class method parse takes in the path to the file and outputs a list
of QuoteModel objects. The each line in the docx file must contain a
quote and an author, seperated by a hyphen.

Requires python-docx to ingest docx file.
"""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.replace('"', '').strip().split('-')
                new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
                quotes.append(new_quote)

        return quotes
