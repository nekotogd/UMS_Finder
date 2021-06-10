# UMS_Finder
A program written in Python using PyTesseract to automatically cross-search the Internet and find answers to your worksheet.

<h2>Written in Python 3.7 and uses some dependencies from versions Python 3.5+ 

  Will not work on Python 2.x 
  
  **(The above only applies to source code users)**

</h2>

<h1>Usage:</h1>

System works based on hotkeys

Q is used to search up questions.
Place your mouse at the top left corner of a piece of text and press Q once. Then place it at the bottom right of the piece of text and press Q again.
Wait a few seconds and your browser should immediately open up with the question searched up on Google.

M is used to find the marking scheme.
Once you have the question paper, make sure to scroll to the first page of the question paper.
Then hit M and watch magic occur.

<h1>Future plans</h1>

Code is kinda ugly ngl. I'm gonna try to cleanup the code in an update.

First though, I want to create an executable but there's some issues with Tesseract when exporting.

<h1>Dependencies for using source code</h1>

* pytesseract https://pypi.org/project/pytesseract/
* keyboard https://pypi.org/project/keyboard/
* pynput https://pypi.org/project/pynput/
* numpy https://pypi.org/project/numpy/
* opencv-python https://pypi.org/project/opencv-python/
* Pillow https://pypi.org/project/Pillow/
* ImageHash https://pypi.org/project/ImageHash/
* pyperclip https://pypi.org/project/pyperclip/
