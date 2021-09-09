"""An abstract class to be realized by other class for ingesting specific
files types

can_ingest is a class method that confims that the file has
the correct extension

The abstract class method parse is to be defined by a child class realizing
this class
"""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
