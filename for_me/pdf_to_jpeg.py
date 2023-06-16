from wand.image import Image
import os
from doc2pdf import convert
import shutil
import random

# Путь для папки, в которой находится python file
file_source = 'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/'

# Путь для папки, в которой находся папки с курсами
file_rasp = f'{file_source}Детское/'

def convert2jpeg(filename):
    """
    .pdf -----> .png with white background
    """
    number = '' # Переменная с рандомным четырехзначным числом для имени
    with Image(filename=filename, format='pdf') as img:
        img.format = 'png'
        img.compression_quality = 100
        for j in range(4):
            i = random.randint(0, 9)
            number += str(i)
        img.save(filename=f'{filename[0:-4]}{number}.png')

    with Image(filename=f'{file_source}back_small.jpg') as background:
        with Image(filename=f'{filename[0:-4]}{number}.png') as foreground:
            background.composite(foreground)
            background.save(filename=f'{filename[0:-4]}{number}.png')

for folder in os.listdir(file_rasp):
    print(folder)
    path = f'{file_rasp}{folder}/'
    os.mkdir(f"{path}photo") # Отключить, если в папках групп уже есть папка с именем "photo"
    for filename in os.listdir(path):
        print(filename)
        if filename.endswith(".doc"):
            convert(f'{path}{filename}')
            
    for filename in os.listdir(path):
        print(filename)
        if filename.endswith(".pdf"):
            convert2jpeg(f'{path}{filename}')
            
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            shutil.move(path + filename, f'{path}photo/' + filename)