import re
import os
import pytesseract
from PIL import Image
from tqdm import tqdm

pytesseract.pytesseract.tesseract_cmd = (
    r"/usr/local/Cellar/tesseract/5.1.0/bin/tesseract"
)
directory = ""


def preprocess_text(text):
    text = text.lower().strip()
    text = re.sub(re.escape("\n"), " ", text)
    return text


def main():
    print("Loading images...")
    file_strings = dict()
    images_paths = [os.path.join(directory, file) for file in os.listdir(directory) if os.fsdecode(file).endswith(".png")]
    for file_path in tqdm(images_paths):
            file_string = pytesseract.image_to_string(file_path)
            file_string = preprocess_text(file_string)
            file_strings[file_path] = file_string
    print("Images loaded.")
    print()
    
    while True:
        print("Introduce phrase:")
        text = input()
        print("")
        print("searching...")
        text = preprocess_text(text)
        files = [
            file_path
            for file_path, image_text in file_strings.items()
            if text in image_text
        ]
        for file in files:
            img = Image.open(file)
            img.show()
        print("DONE")
        print("")


if __name__ == "__main__":
    main()
