# UMS_Finder
A program written in Python using PyTesseract to automatically cross-search the Internet and find answers to your worksheet.

**Written in Python 3.7 and uses some dependencies from versions Python 3.5+. 
Will not work on lower Python versions**
  
**(The above only applies to source code users)**

<h1>Installation</h1>

Head to the right side of this page and you should see a section called "Releases"

Go to the Releases and download 2 files:
* installer.zip
* main_msfinder.exe

Once downloaded, extract installer.zip to **its own folder**

Then run installer.exe
Finally launch main_msfinder.exe and start getting your answers!

<h1>Usage:</h1>

<h3>Finding Questions:</h3>

**Q** is used to search up questions.

Place your mouse at the top left corner of a piece of text and press Q once. Then place it at the bottom right of the piece of text and press Q again.

Wait a few seconds and your browser should immediately open up with the question searched up on Google.

<h3>Finding Marking Schemes:</h3>

**M** is used to find the marking scheme.

Once you have the question paper, make sure to scroll to the first page of the question paper.

Then hit M and watch magic occur.

<h1>Future plans</h1>

Published an update which is fully RegEx based, and makes for much better picking out of the information provided.

Still need to iron out some bugs and make the searching as perfect as possible.

<h1>Dependencies for using source code</h1>

* pytesseract https://pypi.org/project/pytesseract/
* keyboard https://pypi.org/project/keyboard/
* numpy https://pypi.org/project/numpy/
* opencv-python https://pypi.org/project/opencv-python/
* Pillow https://pypi.org/project/Pillow/
* ImageHash https://pypi.org/project/ImageHash/
* pyperclip https://pypi.org/project/pyperclip/
