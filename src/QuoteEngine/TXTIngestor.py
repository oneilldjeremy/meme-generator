"""Opens and ingests the contects of a txt file containing quotes

TXTInvestor realizes the IngestorInterface abstract class.

The class variable allowed_extensions adds txt to the list of allowed
extensions.

The class can run the IngestorInterface class method can_ingest to
confirm the file is a txt.

The class method parse takes in the path to the file and outputs a list
of QuoteModel objects. The each line in the txt file must contain a
quote and an author, seperated by a hyphen.
"""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []

        with open(path, 'r') as infile:

            for line in infile.readlines():
                split_line = line.split('-')
                new_quote = QuoteModel(split_line[0].replace('"', '').strip(),
                                       split_line[1].strip())
                quotes.append(new_quote)

        return quotes
