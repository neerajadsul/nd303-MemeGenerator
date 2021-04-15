from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine():
    font_size = 25
    font = "fonts/Roboto-BoldItalic.ttf"
    MAX_WIDTH = 500

    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Postcard With a Text Greeting

        Arguments:
            in_path {str} -- the file location for the input image.
            text {str} -- quote text
            author {str} -- author name
            width {int} -- maximum width of the generated meme image
        Returns:
            {str} -- the file path to the output image.
        """
        try:
            im = Image.open(img_path)
        except FileNotFoundError:
            print("Input file not found.")    
            return ""
            
        width = self.MAX_WIDTH if width > self.MAX_WIDTH else width
            
        aspect_ratio = width/float(im.size[0])    
        height = int(aspect_ratio*float(im.size[1]))
        im = im.resize((width, height))           
        
        if text is not None and author is not None:                            
            font = ImageFont.truetype(self.font, self.font_size)
            draw = ImageDraw.Draw(im)
            x = 5
            y = random.randint(10,int(0.8*height))
            text_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))
            draw.multiline_text((x, y), f'{text} \n - {author}', font=font, fill=text_color)
        
        self.out_path = os.path.join(
            './static',
            os.path.basename(img_path)
            )

        im.save(self.out_path)
            
        return self.out_path