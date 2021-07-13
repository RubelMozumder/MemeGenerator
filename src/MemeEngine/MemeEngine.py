"""Module to genearate meme.

MemeGenerator class will create a meme from a image in a given path
and save it to the another given path by 'CreateMeme' method.
"""

import os
import random


from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """MemeGenerator class.

    The class creates meme from given image and text.
    The final image is saved to the given path.
    Argument:
        meme_destination (str) : Required to save the mem.
    """

    def __init__(self, meme_destination: str) -> None:
        """Instantiate teh MemeGenerator with path str.

        Argument:
            meme_destination (str) : Path to save the figure.
        """
        self.out_path = meme_destination

    @staticmethod
    def crop_image(in_path: str, width: int = None) -> Image:
        """Crop image.

        Crop the image from image path 'path' according to the
        with given as 'width'.

        Argument:
            in_path (str) : Path to the input figure
            width (int) : Expected width of the output image
        """
        try:
            img = Image.open(in_path)
        except Exception:
            raise OSError('Unable to load the image')

        if width:
            ratio = width/float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        return img

    def make_meme(self, in_path: str, text: str, author: str,
                  width: int = 500) -> str:
        """Create Meme.

        Method make_meme creates meme with the caption 'text' by written
        by 'author'.
        Arguments:
            in_path (str) : Path of image to create meme.
            text (str) : Text to add on the caption.
            author (str) : Name of author.
            width (int) : Width of the new croped imaged without changing
                          aspect ratio of the imput image.
        """
        new_imp = self.crop_image(in_path, width)

        draw = ImageDraw.Draw(new_imp)

        try:
            font = ImageFont.truetype('./_data/fonts/Tangerine-Regular.ttf',
                                      size=30)
        except Exception:
            raise OSError('Invalid font path')

        draw.text((10, 30), text, font=font, fill='blue')
        author = 'by ' + author
        draw.text((10, 55), author, font=font, fill='blue')

        out_path = os.path.join(self.out_path,
                                f'meme_{random.randint(0,100000000)}.png')
        print('This is the print :', out_path)

        new_imp.save(out_path)

        return self.out_path
