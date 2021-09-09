import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine


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
        quote = QuoteModel.QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a meme by overlaying \
                                                  a quotation on to an image.")
    parser.add_argument('--path', type=str, help="The path to the image on \
                                                  your local computer. This \
                                                  path should be either \
                                                  absolute, or relative to \
                                                  the meme.py file. If left \
                                                  blank, a random one will \
                                                  be used.")
    parser.add_argument('--body', type=str, help="The body of the quotation.")
    parser.add_argument('--author', type=str, help="The author of the \
                                                    quotation")

    args = parser.parse_args()

    if (args.path is not None):
        path = os.path.normpath(args.path)
    else:
        path = None

    print(generate_meme(path, args.body, args.author))
