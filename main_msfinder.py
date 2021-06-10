import pyautogui #Make measurements on mouse position and press hotkeys
import keyboard #Write down text
import time #Wait so that we don't run too fast
from pynput.keyboard import Key,Listener #Listen for keypresses and press if we want

import os #Used to find the path of the tesseract
import numpy as nm #Used in the processing of our image into a string
import pytesseract #The main OCR guy
import cv2 #Process Images before handing over to tesseract
from PIL import ImageGrab #Take pictures of portions of our screen
from PIL import Image #Save or load images, used mainly for testing program
import imagehash #Compare images and hash similarity
import re #Heavy text processing workload

import webbrowser #Google up things we need
import pyperclip #Copy and Paste stuff from our clipboard

subject = ''

imageBox = []
sampleText = ''

def hash_similarity(imageA, imageB):
    Ahash = imagehash.average_hash(imageA)
    Bhash = imagehash.average_hash(imageB)
    return (Ahash - Bhash)

def imtostring(x1,y1,x2,y2):
    pytesseract.pytesseract.tesseract_cmd = str(os.getenv('LOCALAPPDATA')) + '/Programs/Tesseract-OCR/tesseract.exe'
    #Image-Grab to capture screen
    #BBox to capture just a specific area
    cap = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    #cap.save("grab.png")

    #Convert to monochrome so it can be read easily
    #Read using OCR and make string of text from it

    #cv2.imwrite("processed.png", cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY))
    tesstr = pytesseract.image_to_string( 
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
            lang ='eng')
    return tesstr

def exist_string(sub_name, string):
    sub_name = sub_name.lower()
    if string.find(sub_name.capitalize()) != -1:
        return True
    elif string.find(sub_name.upper()) != -1:
        return True
    elif string.find(sub_name) != -1:
        return True
    else:
        return False

def google_search_string(inp_string):
    string = re.sub(r'[|?$.]',r'', inp_string)
    string.replace(" ", "+")
    string.replace("(", "%28")
    string.replace(")", "%29")
    string = "\"" + string + "\""
    
    return string

while True:
    pressed_key = keyboard.read_key()
    time.sleep(0.1)
    if pressed_key == "q":
        imageBox.append(pyautogui.position().x)
        imageBox.append(pyautogui.position().y)
        time.sleep(0.2)
    elif pressed_key == "t":
        print(pyautogui.position())
    elif pressed_key == "m":
        qpText = imtostring(0,166,1920,1080)
        sub_list = ["biology", "chemistry", "physics", "mathematics"]
        for sub in sub_list:
            if exist_string(sub, qpText):
                subject = sub.capitalize()

        searchText = ''
        #Do this if CIE Paper
        if exist_string("cambridge", qpText):
            paperCode = 9700
            if qpText.find(str(paperCode)) == -1:
                paperCode = 9701
            pos = qpText.find(str(paperCode)) + 4
            paperNo = str(paperCode) + "/" + qpText[pos+1] + qpText[pos+2]
            month = ""
            yearNo = ""
            years = ["june", "november", "march"]
            for yr in years:
                if exist_string(yr, qpText):
                    month = yr.capitalize()
                    pos = qpText.find(yr.capitalize()) + len(yr)
                    for i in range(5):
                        yearNo += qpText[pos+i]
                        i+=1
                    yearNo = re.sub(r"\s+", "", yearNo)
            
            searchText = "CIE+" + subject + "+" + paperNo + "+MS+" + month + "+" + yearNo

        #Do this if Edexcel Paper
        elif (exist_string("edexcel", qpText) or qpText.find("Edexce") != -1) and qpText.find("Google") == -1:
            print(qpText)
            IALCodes = {
                "Biology" : "WBI",
                "Physics" : "WPH",
                "Chemistry" : "WCH",
                "Mathematics" : "WMA"
                }
            ALCodes = {
                "Biology" : "6BI",
                "Physics" : "6PH",
                "Chemistry" : "6CH",
                "Mathematics" : "8MA"
                }
            MathCodes = ["WMA", "8MA", "666"]
            paperNo = ""
            if qpText.find(IALCodes[subject]) != -1 and subject != "Mathematics":
                pos = qpText.find(IALCodes[subject]) + 3
                paperNo = IALCodes[subject] + qpText[pos] + qpText[pos+1] + "/" + qpText[pos] + qpText[pos+1]
                paperNo = paperNo.replace("O", "0")
            elif qpText.find(ALCodes[subject]) != -1 and subject != "Mathematics":
                pos = qpText.find(ALCodes[subject]) + 3
                paperNo = ALCodes[subject] + qpText[pos] + qpText[pos+1] + "/" + qpText[pos] + qpText[pos+1]
                paperNo = paperNo.replace("O", "0")
            elif subject == "Mathematics":
                for code in MathCodes:
                    if qpText.find(code) != -1:
                        break
                if code == "666":
                    pos = qpText.find(code) + 3
                    paperNo = code + qpText[pos] + qpText[pos+1] + qpText[pos+2] + qpText[pos+3] + qpText[pos+4]
                    paperNo = paperNo.replace("O", "0")
                    paperNo = re.sub(r"\s+", "", paperNo)
                elif code == "WMA":
                    pos = qpText.find(code) + 3
                    paperNo = code + qpText[pos+1] + qpText[pos+2] + qpText[pos+3] + qpText[pos+4] + qpText[pos+5]
                    paperNo = paperNo.replace("O", "0")
                elif code == "8MA":
                    pos = qpText.find(code) + 3
                    paperNo = code + qpText[pos] + qpText[pos+1] + qpText[pos+2] + qpText[pos+3] + qpText[pos+4]
                    paperNo = paperNo.replace("O", "0")

            month = ""
            yearNo = ""
            years = ["january", "february", "may", "june", "october", "november"]
            for yr in years:
                if exist_string(yr, qpText):
                    month = yr.capitalize()
                    pos = qpText.find(yr.capitalize()) + len(yr)
                    for i in range(5):
                        yearNo += qpText[pos+i]
                        i+=1
                    yearNo = re.sub(r"\s+", "", yearNo)

            searchText = "Edexcel+" + subject + "+" + paperNo + "+MS+" + month + "+" + yearNo

        elif exist_string("aqa", qpText) or qpText.find("AQA") != -1:
            AQA_codes = {
                "Biology" : ["BIOL", "7401", "7402"]
                }
            paperNo = ""
            code_list = AQA_codes[subject]
            for code in code_list:
                if qpText.find(code) != -1:
                    paperNo = code
            
            months = ["january", "february", "may", "june", "october", "november"]
            yearNo = ""
            for mt in months:
                if exist_string(mt, qpText):
                    month = mt.capitalize()
                    pos = qpText.find(mt.capitalize()) + len(mt)
                    for i in range(5):
                        yearNo += qpText[pos+i]
                        i += 1
                    yearNo = re.sub(r"\s+", "", yearNo)
                    break
    
            searchText = "AQA+A+Level+" + subject + "+" + paperNo + "+MS+" + month + "+" + yearNo

        else:
            #If neither are found, assume its one of the common sites used by teachers
            pyautogui.press("f6")
            pyautogui.press("f6")
            pyautogui.hotkey("ctrl", "c")
            url = pyperclip.paste()
            if url.find("mathsgenie") != -1:
                pyautogui.press("right")
                for i in range(4):
                    pyautogui.press("left")
                keyboard.write("ans")
                pyautogui.press("enter")
                pos = url.find("resources/") + len("resources/")
                topic = url[pos:]
                get_rid_of = ["as", "stats", "pure",".pdf", "/", "-"]
                for word in get_rid_of:
                    topic = topic.replace(word," ")
                topic = re.sub(r"\s+", " ", topic)
                topic.strip()
                print(topic)
            elif url.find("madasmaths") != -1:
                pyautogui.press("right")
                for i in range(4):
                    pyautogui.press("left")
                keyboard.write("_solutions")
                pyautogui.press("enter")
            elif url.find("books.google") != -1:
                searchText = ''
                bkText = imtostring(30,675,337,729)
                old_mouse_pos = pyautogui.position()
                #83 842
                pyautogui.moveTo(83, 842)
                pyautogui.click()
                pyautogui.moveTo(800,800)
                time.sleep(2)
                pyautogui.scroll(-10000)
                time.sleep(1)
                #385 449 1609 909
                bkText = imtostring(385,449,1609,909)
                temp_str = open('books.txt', 'r').read()
                newText = bkText.split("\n", 11)[11]
                title = newText.partition("\n")[0]
                searchText = google_search_string(title + " Answers")

                #Find ISBN should we need it, no use for it right now tho
                bkText = re.sub(r"\s+", " ", bkText)
                pos = bkText.find("978") + 3
                ISBN = "978"
                for i in range(10):
                    ISBN += bkText[pos]
                    pos += 1
                

        URL = "http://google.com/search?q=" + searchText
        if URL != "http://google.com/search?q=":
            webbrowser.open_new_tab(URL)
    if len(imageBox) == 4:
        sampleText = imtostring(imageBox[0],imageBox[1],imageBox[2],imageBox[3])
        imageBox.clear()

        sampleText = re.sub(r'[|?$.]',r'', sampleText)
        sampleText.replace(" ", "+")
        sampleText.replace("(", "%28")
        sampleText.replace(")", "%29")
        sampleText = "\"" + sampleText + "\""
        
        URL = "http://google.com/search?q=" + sampleText
        webbrowser.open_new_tab(URL)
    pressed_key = ""



