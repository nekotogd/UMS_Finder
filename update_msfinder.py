import ocr_module
import keyboard
import re
import urllib.parse as up
import webbrowser

def find_subject(text):
    subject_list = [
        "mathematics",
        "physics",
        "biology",
        "psychology"
    ]
    for sub in subject_list:
        result = re.search(r"(\b" + sub + r"\b)", text)
        if result is None:
            result = re.search(r"(\b" + sub.upper() + r"\b)", text)
            if result is None:
                result = re.search(r"(\b" + sub.capitalize() + r"\b)", text)
        if not result is None:
            return result[1]
        
    if result is None:
        return ""
    return result

def find_paper_code(text):
    result = re.search(r"(\b[0-9A-Z]{4,}/[0-9]{2,}\b)", text)
    if result is None:
        return ""
    return result[1]

def find_year(text, month):
    result = re.search(month + r"\s*?(20[0-9]{2})", text)
    if result is None:
        return ""
    return result[1]

def find_month(text):
    month_list = [
        "january",
        "february",
        "may",
        "june",
        "october",
        "november"
    ]
    for month in month_list:
        result = re.search(r"(\b" + month + r"\b)", text)
        if result is None:
            result = re.search(r"(\b" + month.upper() + r"\b)", text)
            if result is None:
                result = re.search(r"(\b" + month.capitalize() + r"\b)", text)
        if not result is None:
            return result[1]
    if result is None:
        return ""
    return result[1]

while True:
    pressed_key = keyboard.read_key()
    if pressed_key == "m":
        qp_text = ocr_module.imtostring_array([0, 0, 1920, 1080])
        with open("screen.txt", "w") as f:
            f.write(qp_text)
        subject = find_subject(qp_text)
        paper_code = find_paper_code(qp_text)
        month = find_month(qp_text)
        year = find_year(qp_text, month)
        search_text = " ".join([subject, paper_code, month, year, "MS"])
        search_text = up.quote(search_text)
        URL = "http://google.com/search?q=" + search_text
        webbrowser.open_new_tab(URL)