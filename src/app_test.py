import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
import subprocess

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file)) 

    images_path = './_data/photos/dog/'

    temp_path = images_path+'temp'
    if not os.path.isdir('temp_path'):
        call = subprocess.call(['mkdir', images_path+'temp'])

    imgs = [ f for f in os.listdir(images_path) if len(f.split('.'))>1]
    imgs = [images_path+img for img in imgs]

    if len(imgs)==0:
        raise ValueError('The image sequence is empty')
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """


    img = random.choice(imgs)
    quote = random.choice(quotes)

    file_name = img.split('/')[-1]
    temp_file = 'temp/temp_'+file_name
    out_path = img.replace(file_name, temp_file)
    
    out_path = MemeEngine(out_path).make_meme(img, quote.quote, quote.author)
    
    return render_template('meme.html', path=os.path.abspath(out_path))


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

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    os.remove(tmp)

    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run()
