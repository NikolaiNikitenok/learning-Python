from wand.image import Image
from wand.color import Color
import os
from doc2pdf import convert
import shutil
import random
from PyPDF2 import PdfMerger

start = f'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/Детское/'

os.mkdir(f"{start}all_pdf")
n_path = f'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/Детское/all_pdf/'

for folder in os.listdir('C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/Детское/'):
    print(folder)
    path = f'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/Детское/{folder}/'
    # Конвертируем .док в .пдф
    for filename in os.listdir(path):
        print(filename)
        if filename.endswith(".doc"):
            convert(f'{path}{filename}')
    
    # Переносим пдф в отдельную папку
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            shutil.move(path + filename, n_path + filename)

merger = PdfMerger()

for filename in os.listdir(n_path):
    if filename.endswith(".pdf"):
        merger.append(n_path + filename)

merger.write(n_path + "output.pdf")
merger.close()            
