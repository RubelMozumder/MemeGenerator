"""Module to ingest txt type file.

The module usages the techniuqe as described in abstruct class
IngestorInterface.
"""


from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import os


class TEXTIngestor(IngestorInterface):
    """Class TXTIngestor.

    The class manipulate the txt type file, parse the quote and auther
    and retrun the QuoteModel object list.
    """

    allowed_file_extention: List[str] = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file.

        The classmethod 'parse()' extract the 'quote' and Author
        returns the list of QuoteModel.
        Parameters:
            path (str) : path of 'txt' file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            if cls.can_ingest(path):
                quote_list: List[QuoteModel] = []
                with open(path, 'r') as txt_obj:
                    lines = txt_obj.readlines()
                    for line in iter(lines):
                        line = line.strip('\n\r').strip()
                        if len(line) < 3:
                            continue
                        quote, author = tuple(line.split(' - '))
                        quote_list.append(QuoteModel(quote, author))

            return quote_list
        except Exception:
            msg = ("Check the file path. Maybe the file "
                   "path is not correct.")
            raise OSError()
