"""Module to check to choose teh appropriate helper function.

The module usages the techniuqe as described in abstruct class
IngestorInterface and call appropriate helper class from
DOCXIngestor, PDFIngestor, TEXTIngestor and CSVIngestor.
"""


from .IngestorInterface import IngestorInterface
from typing import List
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TEXTIngestor import TEXTIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Class Ingestor.

    To select and call the helper class from DOCXIngestor,
    CSVIngestor, PDFIngestor TEXTIngestor
    """

    ingestors = [DOCXIngestor, CSVIngestor, TEXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse correct file from appropriate helper class.

        Parameters:
            path (str) : path of csv csv file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    quote_model_list = ingestor.parse(path)

            return quote_model_list
        except Exception:
            msg = ("Check the file path. Maybe the file "
                   "path is not correct.")
            raise OSError()
