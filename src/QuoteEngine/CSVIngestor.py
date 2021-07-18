"""Module to ingest csv type file.

The module usages the techniuqe as described in abstruct class
IngestorInterface.
"""


from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import csv


class CSVIngestor(IngestorInterface):
    """Class CSVIngestor.

    The class manipulate the csv type file, parse the quote and auther
    and retrun the QuoteModel object list.
    """

    allowed_file_extention: List[str] = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file.

        The classmethod 'parse()' extract the 'quote' and Author
        return the list of QuoteModel.
        Parameters:
            path (str) : path of csv csv file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            if cls.can_ingest(path):
                quote_list: List[QuoteModel] = []
                with open(path, 'r') as csv_obj:
                    reader = csv.reader(csv_obj)
                    next(reader, None)
                    for row in iter(reader):
                        quote_list.append(QuoteModel(row[0], row[1]))

            return quote_list
        except Exception:
            msg = ("Check the file path. Maybe the file "
                   "path is not correct.")
            raise OSError()
