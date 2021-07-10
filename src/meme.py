import os
import random
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
import argparse
from QuoteEngine import QuoteModel

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    out_path = './generated_' + img.split('/')[-1]
    meme = MemeEngine(out_path)
    path = meme.make_meme(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description= 'To create Meme from the given figure, quote and author')
    parser.add_argument('--path', help='Figure path', default= None)
    parser.add_argument('--body', help='Body text to be anchored on the figure', default=None)
    parser.add_argument('--author', help='Author of the body text', default= None)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
