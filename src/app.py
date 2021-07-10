import random
import os
import requests
from flask import Flask, render_template, abort, request

import subprocess

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
       
    imgs = [ f for f in os.listdir(images_path) if len(f.split('.'))>1]
    imgs = [images_path+img for img in imgs]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    
    img_file = img.split('/')[-1]
    img_path = img.replace(img_file,'')
    if not os.path.isdir(img_path+'tmp'):
        call = subprocess.call(['mkdir', img_path+'tmp'])
    
    out_path = img.replace(img_file,'tmp/temp_'+img_file)
    path = MemeEngine(out_path).make_meme(img, quote.quote, quote.author)
   
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    
    image_url = request.form.get('image_url')
    tmp = f'./temp_{random.randint(0, 1000000)}.png'
    with open(tmp, 'wb') as img_f:
        img_f.write(image_url.content)
    
    quote = request.form.get('quote', "")
    author = request.form.get('author', "")
    img_file = tmp.split('/')[-1]
    meme_file = 'out_'+ img_file
    out_path = tmp.replace(img_file, meme_file)
    path = MemeEngine(out_path).make_meme(tmp, quote, author)


    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
