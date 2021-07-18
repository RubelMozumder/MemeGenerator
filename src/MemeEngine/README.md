#Module MemeEngine

The submodule MemeEngine includes `MemeEngine(out_path)` can be instantiate to recreate the given figure with the text written ove it.

##Methods:

`crop_image(self, in_path, width)`: 
returns croped image which is croped according to width and the image provided by user via `in_path`. The methode also maintains ratio of image size.

`make_meme(self, in_path, text, author, and width)`:
Returns the meme file path (`out_path`) to the predefined output path provided on the class instantiate.
`

## Usages:
The following code snippet is tested from the `<package root>/scr/MemeEmgine`.

```
In [3]: import MemeEngine                                                                  

In [5]: out_path = './'                                                                    

In [6]: in_path = './_data/photos/dog/xander_3.jpg'                                        

In [7]: output = MemeEngine.MemeEngine(out_path).make_meme(in_path, text= 'The purpose of o
   ...: ur life is to be happy', author= 'DALAI LAMA', width= 400)                         
This is the print : ./meme_90566441.png
```

## Conclusion:

The package generate the meme based on the user given figure paths (input and ouput), width, text, and author.
