"""This class contains the make_meme method, which will overlay text
on an image when provided with an image, quote, and author.

This method requires an img_path, text, and author, with an optional
argument for the width of the image. This method utilizes the Pillow
module to appropriately size the image and overlay the image with text.

It returns the location of the generated image.
"""
from PIL import Image, ImageDraw, ImageFont
import random
import os
from math import ceil


class MemeEngine:

    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Create a meme with overlayed text

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the quotation text to be overlayed.
            author {str} -- the quotation's author
            width {int} -- the pixel width of the image. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        allowed_extensions = ['jpg', 'png', 'gif']
        
        img_path = os.path.normpath(img_path)
        file_name = os.path.basename(img_path)
        ext = file_name.split('.')[-1]
        
        if ext not in allowed_extensions:
            raise Exception("File type must be jpg, png, or gif")

        if (width > 500):
            raise Exception("Width must be less than or equal to 500")

        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)

        '''Confirm text and author will fit at smallest size'''
        text_width = ImageFont.truetype('arial.ttf',
                                        size=2).getsize(text)[0]
        author_width = ImageFont.truetype('arial.ttf',
                                          size=1).getsize('-' + author)[0] + 2

        if (text_width > img.size[0] or author_width > img.size[0]):
            raise Exception("Text is too long")

        '''Test for appropriate font size'''
        font_test = 0
        text_test = 0
        author_test = 0
        author_padding_test = 0

        while (font_test <= 50 and
               (text_test <= img.size[0] and
                author_padding_test <= img.size[0])):

            font_test += 1

            text_test = ImageFont.truetype('arial.ttf',
                                           size=font_test).getsize(text)[0]
            author_test = ImageFont.truetype('arial.ttf',
                                             size=font_test).getsize(
                                                  '-' + author)[0]

            author_padding_test = author_test + font_test

        font_size = font_test - 1

        text_font = ImageFont.truetype('arial.ttf', size=font_size)
        author_font = ImageFont.truetype('arial.ttf', size=ceil(font_size/2))

        text_width = text_font.getsize(text)[0]
        author_width = author_font.getsize(text)[0]
        text_height = text_font.getsize(text)[1]
        author_height = author_font.getsize(text)[1]

        x_coordinate_text = random.randint(0, img.size[0] -
                                           max(text_width,
                                               author_width + font_size))
        y_coordinate_text = random.randint(0, img.size[1] -
                                           (text_height + author_height +
                                           ceil((1/5) * font_size)))

        x_coordinate_author = x_coordinate_text + font_size
        y_coordinate_author = (y_coordinate_text + text_height +
                               ceil((1/5) * font_size))

        draw.text((x_coordinate_text, y_coordinate_text),
                  text, font=text_font, fill='red')
        draw.text((x_coordinate_author, y_coordinate_author),
                  '-' + author, font=author_font, fill='red')

        filename = f'{random.randint(0,1000000)}.jpg'

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        filepath = self.output_dir + '/' + filename

        if os.path.exists(filepath):
            os.remove(filepath)

        img.save(filepath)
        return filepath
