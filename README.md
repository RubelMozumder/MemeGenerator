# Meme Generator:
This project has two parts
## Quote Engine:
**`QuoteEngine`** is elegible to parse the Quote and the corrsponding Author from the pdf, csv, text and docx extention files. The module mainly builds on the `Stratagy Object` approachcreated with help of `abstrctclass` [IngestorInterface](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/IngestorInterface.py). Any of the files as mentioned above can be paserd via `parse(path: str)` from sub-module [Ingestor](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/Ingestor.py) (QuoteEngine.Ingestor.parse(path)). The sub-module choose the appropriate module ([PDFIngestor](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/PDFIngestor.py), [CSVIngestor](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/CSVIngestor.py), [TEXTIngetor](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/TEXTIngestor.py) & [DOCXIngestor](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/DOCXIngestor.py) ) need to parse the provided file as input in `parse(path)` method and return list of `QuoteModel` [QuoteModel](https://github.com/RubelMozumder/MemeGenerator/blob/read_data/src/QuoteEngine/QuoteModel.py) objects. Each Object of the `QuoteModel` belongs two attributes `quote & author`.

### Usages of `QuoteEngine` module:
Example: The example below is run from the `/scr` directory 
```
In [4]: import QuoteEngine as Q                                                            

In [5]: path = './_data/DogQuotes/DogQuotesCSV.csv'                                        

In [6]: objs = Q.Ingestor.parse(path)                                                      

In [7]: objs[0].quote                                                                      
Out[7]: 'Chase the mailman'

In [8]: objs[0].author                                                                     
Out[8]: 'Skittle'

```

## MemeEngine:

### TODO: also add one picture using both module `QuoteEngine & MemeEngine`
The work anchors quote and the corresponding author on a croped pictures. 
