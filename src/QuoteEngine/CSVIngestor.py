"""Opens and ingests the contects of a csv file containing quotes

CSVInvestor realizes the IngestorInterface abstract class.

The class variable allowed_extensions adds csv to the list of allowed
extensions.

The class can run the IngestorInterface class method can_ingest to
confirm the file is a csv.

The class method parse takes in the path to the file and outputs a list
of QuoteModel objects. The each line in the csv file must contain a
quote and an author, seperated by a comma.

Requires pandas to process csv file.
"""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'].replace('"', '').strip(),
                                   row['author'].strip())
            quotes.append(new_quote)

        return quotes
