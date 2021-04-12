Overview of the project
=======================
The project contains code to generate a meme. It has two modes of operation.

*The command line* based version uses locally stored images to generate a meme using user supplied body text and author name. The meme is stored locally as a file and path to the file is displayed to the user.

*The web based* version can create a new meme based on user supplied image url, quote and author via a web form.
Alternatively it can generate a random meme from local images, collection of quotes and authors.
The meme is displayed in the web browser.

Instructions for setting up and running the app
===============================================

Project Setup
-------------

1. Clone repository or download as a zip file.
2. From the terminal, navigate to the projects working directory `path to project\meme_generator`
3. Create a virtual environment for the project using Python 3.6+ 
4. Activate the created virtual environment
4. Use `requirements.txt` to install the dependencies for the project.

Running the app
---------------

**Command line version**
Use `python meme.py -h` to find the usage documentation.

The `python meme.py` the app will randomly select image or quote or the author or all the not supplied arguemnts to generate the meme. The meme image path will be displayed on the command line.

**Web based version**
Set the environment variable `FLASK_APP=app.py`

Then run command `flask run` to start the app server. Use the information displayed in the terminal to open the app in the web browser. Typically it will be pointing at `http://127.0.0.1:5000/`.

Sub-modules Documentation
=====================

Module `QuoteEngine`

Role and Responsibility
Dependencies
Examples

Module `MemeEngine`

Role and Responsibility
Dependencies
Examples
