'''
UMS Finder Installer for Tesseract-OCR
'''

import tkinter as tk #Used for prompting the user for installation directory
from tkinter import filedialog as fd
import pathlib #Used to get location of the installer file
import zipfile #To extract the bundled Tesseract archive into a directory
import os #Used to get localappdata folder
import glob #Used for deleting files

def delete_dir_files(directory):
    if not type(directory) is str:
        directory = str(directory)
    [f.unlink() for f in pathlib.Path(directory).glob("*") if f.is_file()]
    print("directory cleared")
    return True

def unzip(zip_path, extraction_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extraction_path)
        zip_ref.close()
    print("extraction done")
    return True

def browse_file():
    file_path = fd.askopenfilename(
        title = "Open a File",
        filetypes=(("PNG Files","*.png"),("All files","*.*")),
        initialdir = pathlib.Path().absolute())
    print(file_path)
    return file_path

def browse_directory():
    dir_path = fd.askdirectory(
        mustexist = True,
        initialdir = pathlib.Path().absolute())

    #In case user hits cancel button, dont delete anything and instead return
    if not type(dir_path) is str:
        dir_path = str(dir_path)
    if dir_path == str(pathlib.Path().absolute()):
        print("halted self")
        return
    if dir_path == "":
        print("halted self")
        return
        
    print(dir_path)
    window.destroy()
    delete_dir_files(dir_path)
    unzip("Tesseract-OCR.zip", dir_path)
    return dir_path

window = tk.Tk()

def install():
    window.destroy()
    
    tesseract_dir = str(os.getenv('LOCALAPPDATA')) + '/Programs/'
    tesseract_dir = os.path.join(tesseract_dir, "Tesseract-OCR")
    if not os.path.isdir(tesseract_dir):
       os.mkdir(tesseract_dir)
    
    ok = True
    ok = delete_dir_files(tesseract_dir)
    if not ok:
        return
    ok = os.path.isfile("Tesseract-OCR.zip")
    if not ok:
        return
    unzip("Tesseract-OCR.zip", tesseract_dir)
    exit()
    return

label1 = tk.Label(window, text = "Gonna ask few questions to make sure installation doesnt mess up")
label2 = tk.Label(window, text = "Is there a file called Tesseract-OCR.zip in this folder?")
label3 = tk.Label(window, text = "If this was installed previously, all files will be cleared and started anew")
label4 = tk.Label(window, text = "The installation will take place in this folder:")
label5 = tk.Label(window, text = str(os.getenv('LOCALAPPDATA')).replace("\\", "/") + '/Programs/Tesseract-OCR')
label6 = tk.Label(window, text = "If you are ready for installation click the button")
label7 = tk.Label(window, text = "If you wish to cancel simply close the window and the installation will abort")
button = tk.Button(window, text = "Install!", command = install)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
button.pack()

window.mainloop()














