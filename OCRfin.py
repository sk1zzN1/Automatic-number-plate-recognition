import os
import cv2
import easyocr
from rapidfuzz import fuzz
import subprocess

import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGES_DIR = os.path.join(BASE_DIR, "images")
WHITE_LIST = os.path.join(BASE_DIR, "white_list.txt")
BLACK_LIST = os.path.join(BASE_DIR, "black_list.txt")
GRAY_LIST = os.path.join(BASE_DIR, "gray_list.txt")


ocr = easyocr.Reader(['en'])

def call_gray_writer(text):
    subprocess.run(["gray_writer.exe", GRAY_LIST, text], check=True)

def load_list(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def similar_enough(text, ref_list, threshold=70):
    return any(fuzz.ratio(text, ref) >= threshold for ref in ref_list)

def ocr_texts(img):
    inv = cv2.bitwise_not(img)
    return [txt.replace(" ", "") for _, txt, _ in ocr.readtext(inv)]

def process_file(fname, white_list, black_list):
    path = os.path.join(IMAGES_DIR, fname)
    img = cv2.imread(path)
    if img is None:
        print(f"Could not open {fname}")
        return

    texts = ocr_texts(img)

    for t in texts:
        if similar_enough(t, white_list):
            print(f"[{fname}] {t} ✅ in white list")
        elif similar_enough(t, black_list):
            print(f"[{fname}] {t} ❌ in black list (ignored)")
        else:
            call_gray_writer(t)
            print(f"[{fname}] {t} ⚠️ added to gray list")


def main():
    white_list = load_list(WHITE_LIST)
    black_list = load_list(BLACK_LIST)

    files = filter(lambda f: f.startswith("Cars") and f.endswith(".png"), os.listdir(IMAGES_DIR))
    for f in files:
        process_file(f, white_list, black_list)

if __name__ == "__main__":
    main()
