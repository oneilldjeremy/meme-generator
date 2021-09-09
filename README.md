Meme Generator
--------------

## Introduction

This application generates a meme consisting of text overlaid on an image. You are able to generate memes by applying random quotations written to several file types and overlaying the text on to a random image from a folder of images. You are also able to build your own meme using an image from the web or saved to your local computer.

The application can be run on a Flask server and accessed via a web browser, or via your computer's command line.

When generating a random meme, the applcation will obtain a random quote saved to a file in the ./_data/DogQuotes folder. The text can be written to the following file types: .txt, .csv, .docx, .pdf. The quote should also be followed by an author name, with the two seperated by a hyphen (for .txt, .docx, or .pdf) or a comma (for .csv). The images are randomly selected from the ./_data/photos/dogs folder.

You can also create our own meme using two different methods. Via the command line, you can provide an image saved to your local computer to utilize, along with an author and a quote. Via the browser, you can provide an image from a URL.

## Dependencies

  * **virtualenv** as a tool to create isolated Python environments
  * **Python3** to run the command line application and server language 
  **Flask** as our server language and server framework
  **pdftotext** - for Linux, install pdftotext. For Windows, install xpdfreader

## To Run

Initialize and activate a virtualenv:

python -m virtualenv env
source env/bin/activate

Install the dependencies:

pip install -r requirements.txt

Run the development server:

Change directory to root of application
export FLASK_APP=app
python app.py

Run command line application:

Change directory to root of application
python meme.py

## Main Files: Project Structure

  ```src
  ├── README.md
  ├── _data *** Hold the data utilized by the random meme generator. Files with quotes can be added to DogQuotes folder, images can be added to photos
  ├── MemeGenerator *** Generates a meme when provided with an image and quote
  │   ├── __init__.py
  │   └── MemeEngine.py
  ├── QuoteEngine *** A module that can process a variety of files to obtain text to be implemented as a quote
  │   ├── __init__.py
  │   ├── CSVIngestor.py
  │   ├── DocxIngestor.py
  │   ├── Ingestor.py
  │   ├── IngestorInterface.py
  │   ├── PDFIngestor.py
  │   ├── QuoteModel.py
  │   └── TTXTModel.py
  ├── static *** Holds images generated in browser
  ├── templates *** Holds html file
  ├── tmp *** Holds images created via command line
  ├── app.py *** Run python app.py to start web server.
  ├── meme.py *** Run via command line.
  └── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt

## Modules:

MemeGenerator: Generates a meme when provided with an image and quote

	MemeEnginer.py: A class that is initialized with an output destination for the generated meme. Once initialized, can execute the make_meme method to create the meme. 

		make_meme(): This method requires an img_path, text, and author, with an option argument for the width of the image. This method utilizes the Pillow module to appropriately size the image and overlay the image with text. 			     It returns the location of the generated image.

		Example: meme = MemeEngine('./tmp')
		 	 return_dir = meme.make_meme('./_data/photos/dog/xander_1.jpg', 'Bark', 'Spot')

QuoteEngine: A module that can process a variety of files to obtain text to be implemented as a quote

	IngestorInterface: An abstract base class that creates the structure for other classes in the module that will ingest specific file types.
	
	CSVIngestor: A class that realizes the IngestorInterface for .csv files. It will confirm the file is .csv, and ingest the contents of the csv to create a QuoteModel object. Requires panda.

	DocxIngestor: A class that realizes the IngestorInterface for .docx files. It will confirm the file is .docx, and ingest the contents of the csv to create a QuoteModel object. Requires docx.

	PDFIngestor: A class that realizes the IngestorInterface for .pdf files. It will confirm the file is .pdf, and ingest the contents of the pdf to create a QuoteModel object. It utilizes the pdftotext command line utility.

	PDFIngestor: A class that realizes the IngestorInterface for .pdf files. It will confirm the file is .pdf, and ingest the contents of the pdf to create a QuoteModel object.

	TXTIngestor: PDFIngestor: A class that realizes the IngestorInterface for .txt files. It will confirm the file is .txt, and ingest the contents of the pdf to create a QuoteModel object. 

	Ingestor: Aggregates the four specific file type ingestors. Will parse a file provided in the class method parse, and return a list of QuoteModel objects.

	QuoteModel: A simple object with variables for quote text and author.


	Example: quotes = Ingestor.parse(./quotes.(txt|csv|docx|pdf)
	
		



  