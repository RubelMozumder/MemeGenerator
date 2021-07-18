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

## To create meme randomly or on intended picture
Run the app from `src` directory.
```
python3 app
```
Then copy the link past it on the google browser.
Some free figure links are here

1. [picturei1](https://images.ctfassets.net/2y9b3o528xhq/5sXS0Rr3MEr66P5elfYX7P/3728cc2d85c0979cb29d5cb291369038/mentor.jpg)
2. [picture2](https://images.ctfassets.net/2y9b3o528xhq/5p7HANmA1jsw8P9EVOeVso/cbfa17357399d99a76d641c777e81a81/self-paced.png)

### Dependencies
Requirements:

	1. PIL: [pillow](https://pillow.readthedocs.io/en/stable/installation.html)
	2. DOCX: [docx](https://python-docx.readthedocs.io/en/latest/user/install.html)
	3. Xpdf:
		For Ubuntu:
		```
		$ wget http://security.ubuntu.com/ubuntu/pool/main/p/poppler/libpoppler73_0.62.0-2ubuntu2.12_amd64.deb
		  
		$ sudo apt-get install ./libpoppler73_0.62.0-2ubuntu2.12_amd64.deb
		$ wget http://archive.ubuntu.com/ubuntu/pool/universe/x/xpdf/xpdf_3.04-7_amd64.deb
		$ sudo apt-get install ./xpdf_3.04-7_amd64.deb
		```
		or 
follow [here](https://www.xpdfreader.com/about.html)
	4. [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
		
## Acknowledgement:
[Udacity](https://www.udacity.com/)
