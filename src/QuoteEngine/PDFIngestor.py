"""Module to ingest pdf type file.

The module usages the techniuqe as described in abstruct class
IngestorInterface.
"""


from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import subprocess
import os
import random


class PDFIngestor(IngestorInterface):
    """Class PDFIngestor.

    The class manipulate the pdf type file, parse the quote and auther
     and retrun the QuoteModel object list.

    """

    allowed_file_extention: List[str] = ['pdf']

    @staticmethod
    def pdftotxt(path: str) -> str:
        """Convert pdf to txt file.

        parameters:
            path (str): path of pdf.
        return:
            path (str) : path of created txt file.
        """
        txt_file = f'./{random.randint(0, 10000000)}.txt'

        try:
            popen = subprocess.Popen(['touch', txt_file])
            call = subprocess.call(['pdftotext', path, txt_file],
                                   stderr=subprocess.STDOUT)
            return txt_file
        except Exception:
            os.remove(txt_file)
            msg = ("Somthing wrong with the given file path"
                   "or conversion from pdf to txt.")
            raise OSError()

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

                path = cls.pdftotxt(path)
                quote_list: List[QuoteModel] = []
                with open(path, 'r') as txt_obj:
                    lines = txt_obj.readlines()
                    for line in iter(lines):
                        line = line.strip('\n\n').strip()
                        if len(line) < 3:
                            continue
                        quote, author = tuple(line.split(' - '))
                        quote_list.append(QuoteModel(quote, author))
            os.remove(path)
            return quote_list
        except Exception:
            msg = ("Check the file path. Maybe the file "
                   "path is not correct.")
            raise OSError()
