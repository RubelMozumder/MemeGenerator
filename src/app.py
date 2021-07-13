"""Module for web-app."""


import random
import os
import requests
from flask import Flask, render_template, abort, request

import subprocess

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('../static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = [f for f in os.listdir(images_path) if len(f.split('.')) > 1]
    imgs = [images_path+img for img in imgs]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)

    out_path = meme.make_meme(img, quote.quote, quote.author)

    return render_template('meme.html', path=os.path.relpath(out_path))


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    r = requests.get(image_url, allow_redirects=True)

    tmp = f'./temp_{random.randint(0, 1000000)}.png'
    with open(tmp, 'wb') as img_f:
        img_f.write(r.content)

    quote = request.form.get('quote', "")
    author = request.form.get('author', "")

    path = meme.make_meme(tmp, quote, author)

    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
