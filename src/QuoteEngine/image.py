from PIL import Image
import random 


def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    # Load the image
    img = Image.open(in_path)

    
    
    raise Exception('generate_postcard not implemented')

if __name__=='__main__':
    out_path = f'./{random.randint(0,1000000)}.png'
    print(generate_postcard('./xander_1.jpg', out_path))
