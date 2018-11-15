#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     recognize_char
    Author:        WYB
    Date:          2018/11/14 20:59:05
    Description:   python 图像识别
"""
import os, sys
from PIL import Image
import pytesseract
# https://blog.csdn.net/dcba2014/article/details/78969658

# 1、下载tesseract.exe
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.01.exe
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files\\tesseract-ocr\\tesseract-3.0.2\\Tesseract-OCR\\tesseract.exe'
# 2、下载tessdata 数据包
# git clone https://github.com/tesseract-ocr/tesseract.git
# tessdata_dir_config = '--tessdata-dir "E:\\Program Files\\Python3\\data\\tessdata"'
# 3、使用
def get_text(file):
    text=pytesseract.image_to_string(Image.open(file),lang='eng')
    print("result:",text)
    return text


# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
#
# # If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#
# # Simple image to string
# print(pytesseract.image_to_string(Image.open('1.png')))
#
# # French text image to string
# print(pytesseract.image_to_string(Image.open('1-european.jpg'), lang='fra'))
#
# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('1.png')))
#
# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('1.png')))
#
# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('1.png')))
#
# # In order to bypass the internal image conversions, just use relative or absolute image path
# # NOTE: If you don't use supported images, tesseract will return error
# print(pytesseract.image_to_string('1.png'))
#
# # get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('1.png', extension='pdf')
#
# # get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('1.png', extension='hocr')
    