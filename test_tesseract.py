# https://golos.io/vox-populi/@vp-webdev/raspoznavanie-teksta-na-izobrazhenii

'''
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-rus
sudo apt-get install python3-pip

pip install pytesseract
pip install tesseract
pip install tesseract-ocr 
pip install pillow
'''

# Можно также добавить фильтры из OpenCV

from PIL import Image
import pytesseract

if __name__ == '__main__':
    f= open('text_photo.txt','w')
    #получаем текст из фото
    text = pytesseract.image_to_string(Image.open('test1.jpg'), lang='eng')
    #записываем его
    f.write(text)
