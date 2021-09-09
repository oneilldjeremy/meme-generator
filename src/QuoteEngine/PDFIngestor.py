"""Opens and ingests the contects of a csv file containing quotes

PDFInvestor realizes the IngestorInterface abstract class.

The class variable allowed_extensions aadds pdf to the list of allowed
extensions.

The class can run the IngestorInterface class method can_ingest to
confirm the file is a pdf.

The class method parse takes in the path to the file and outputs a list
of QuoteModel objects. The each line in the csv file must contain a
quote and an author, seperated by a comma
"""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
      
        if not os.path.exists('./tmp'):
            os.makedirs('./tmp')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        subprocess.run(['pdftotext', '-layout', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0].replace('"', '').strip(),
                                       parsed[1].strip())
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
