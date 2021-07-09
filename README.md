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
### Dependencies:
Requirements:

	1. [subprocess](https://docs.python.org/3/library/subprocess.html)
	2. [python-docx](https://python-docx.readthedocs.io/en/latest/user/install.html)

System needs [XpdfReader](https://www.xpdfreader.com/about.html) installed.

## MemeEngine:
The MemeEngine is build up to work with picture, qoute and the auther of the quote. The general functionality of this module is to receive the picture, quote, and author and return picture with quote and author anchored on it.
The module also allows to crop the given picture via the parameter `width` of `make_meme()` method.

### Usaes of `MemeEngine` module:

Example: The example below is run from the `/src` directory
```In [2]: import MemeEngine                                                                  

In [3]: import MemeEngine as m                                                             

In [4]: in_path = './_data/photos/dog/xander_2.jpg'                                        

In [6]: out_path = './test_meme.jpg'                                                       

In [7]: quote = 'United we stand, divided we fall.'                                        

In [8]: author = 'Aesop'                                                                   

In [10]: m.MemeEngine(out_path).make_meme(in_path=in_path, text=quote,  
    ...:                                  author=author, width=400) 
Out[10]: './test_meme.jpg'
```
![imgur](./src/test_meme.jpg)

### Dependencies
Requirements:

	1. [PIL] [pillow](https://pillow.readthedocs.io/en/stable/installation.html)
