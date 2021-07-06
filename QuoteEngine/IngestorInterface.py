"""Module IngestorInterface.
Module encapsulates IngestorInterface class with all the generic 
'abstractmethods' and 'classmethods'.
"""


from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """Abstractclass IngestoInterface."""

    allowed_file_extention = []
    
    @abstractclass
    def parse(cls, path: str) -> List[QuoteModel]:
        "parse function should be implemented at the stratgy class"
        pass

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        "can_ingest classmethod will check for correct file extension"
        extention = path.split('.')[-1]
        return extention in allowed_file_extention
            
