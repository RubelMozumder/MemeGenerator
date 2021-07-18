# QuoteEngine Module:
The module collect codes and author from the file with extention `.csv`, `.pdf`, `.txt` and `.docx` and able to create `QuoteModel` object. The `QouteModel` (using the `QuoteModel` submodule) object has two attribute `quote` and `author`.

## Submodules:
### `IngestorInterface`: 
The submodule is the abstract class (Template class) for all `Ingestor` type module. It has two methods `parse()` and `can_ingest()`. The `parse(self, path)` method should be construct in all `Ingestor`type module. The method returns list `QuoteModel` objects. The `can_ingest` method check the given file is from the  allowed file extention or not and return for allowed file extension.
### `CSVIngestor`:
 The `CSVIngestor` submoule is the child submodule of submodule `IngestorInterface`. The submodule implies the `can_ingest()` method and construct the `parse()` method for the `csv` type file. Finally return list of `QuoteModel` object.
### `PDFIngestor`:
 The `PDFIngestor` submoule is the child submodule of submodule `IngestorInterface`. The submodule implies the `can_ingest(path)` method and construct the `parse(self, path)` method for parseing the `pdf` type file. Finally return list of `QuoteModel` objects.
### `TEXTIngetor`:
 The `TEXTIngetor` submoule is the child submodule of submodule `IngestorInterface`. The submodule implies the `can_ingest(path)` method and construct the `parse(self, path)` method for parseing the `txt` type file. Finally return list of `QuoteModel` objects.
### `DOCXIngetor`:
 The `DOCXIngetor` submoule is the child submodule of submodule `IngestorInterface`. The submodule implies the `can_ingest(path)` method and construct the `parse(self, path)` method for parseing the `docx` type file. Finally return list of `QuoteModel` object.
### `Ingestor`:
The submodule `Ingestor` check the given file extension and select the apropriate ingestor and execute it.
### `QuoteModel`:
The `QuoteModel` has two attributes `quote` and `author` which reserve the text and the corresponding author. This submodule have also `quote_parser` classmethod.

## Usages:
The following code snipet is run from the `<package root directory>/src`

```
In [1]: import QuoteEngine                                                                 

In [2]: pdf = './_data/DogQuotes/DogQuotesPDF.pdf'                                         

In [4]: quote_list = QuoteEngine.Ingestor.parse(pdf)                                       

In [5]: len(quote_list)                                                                    
Out[5]: 3

In [6]: print(quote_list[0])                                                               
Quote : "Treat yo self", Author : Fluffles

```
## Summary:
Though it is possible to call `parse()` method from all the submodules but `Ingettor.parse()` is the best option and build for general call indtead individual calling.
