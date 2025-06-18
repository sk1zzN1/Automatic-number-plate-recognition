import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os
import cv2
import sys
import OCRfin
from OCRfin import ocr_texts, load_list, similar_enough, call_gray_writer, IMAGES_DIR, WHITE_LIST, BLACK_LIST


class App:
    def __init__(self, root):
        self.root = root
        self.white_list = load_list(WHITE_LIST)
        self.black_list = load_list(BLACK_LIST)
        self.files = [f for f in os.listdir(IMAGES_DIR) if f.startswith("Cars") and f.endswith(".png")]
        self.index = 0

        self.img_label = Label(root)
        self.img_label.pack()
        self.result_label = Label(root, text="", font=("Arial", 16))
        self.result_label.pack()
        Button(root, text="Următoarea imagine", command=self.next_image).pack()

        self.next_image()

    def next_image(self):
        if self.index >= len(self.files):
            self.result_label.config(text="Sfârșit.")
            return

        fname = self.files[self.index]
        img_path = os.path.join(IMAGES_DIR, fname)
        img_cv = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil.resize((500, 300)))
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

        texts = ocr_texts(img_cv)
        status = "❌ Necunoscut"
        for t in texts:
            if similar_enough(t, self.white_list):
                status = f"✅ {t} în white list"
                break
            elif similar_enough(t, self.black_list):
                status = f"❌ {t} în black list"
                break
            else:
                call_gray_writer(t)
                status = f"⚠️ {t} adăugat în gray list"

        self.result_label.config(text=status)
        self.index += 1

root = tk.Tk()
root.title("Recunoaștere numere auto")
app = App(root)
root.mainloop()
