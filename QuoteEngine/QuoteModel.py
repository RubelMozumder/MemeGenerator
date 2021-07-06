"""Module for encapsulating Quote and Author."""


class QuoteModel:
    """Class for collect the Quote and Author.

    Arguments:
        quote (str) -> Quote body.
        author (str) -> Name of Author of the citation

    Return:
        QuoteModel object.

    Usages:
        QuoteModel(quote, author) -> Instantiate QuoteModel object
    or,
        QuoteModel.quote_parser(quote, author) ->
                            Instantiate QuoteModel Object
    """

    def __init__(self, quote: str, author: str) -> None:
        """Parameters: quote(str), author(str).

        Return: its own instantiated object
        """
        self.quote = quote
        self.author = author

    @classmethod
    def quote_parser(cls, quote: str, author: str) -> object:
        """parameter: quote(str), author(str).

        Return: instantiated QuoteModel object
        """
        return cls(quote, author)
