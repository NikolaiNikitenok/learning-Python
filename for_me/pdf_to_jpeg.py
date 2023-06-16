from wand.image import Image
from wand.color import Color
import os
from doc2pdf import convert
import shutil
import random

file_source = 'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/'
file_destination = 'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/finish/'

def convert2jpeg(filename):
    number = ''
    with Image(filename=filename, format='pdf') as img:
        img.format = 'png'
        img.compression_quality = 100
        for j in range(4):
            i = random.randint(0, 9)
            number += str(i)
        img.save(filename=f'{filename[0:-4]}{number}.png')

    with Image(filename='back_small.jpg') as background:
        number = ''
        with Image(filename=f'{filename[0:-4]}.png') as foreground:
            for j in range(4):
                i = random.randint(0, 9) 
                number += str(i)
            background.composite(foreground)
            background.save(filename=f'{filename[0:-4]}{number}.png')
            
# for filename in os.listdir():
#     if filename.endswith(".doc"):
#         convert(filename)
        
# for filename in os.listdir():
#     if filename.endswith(".pdf"):
#         convert2jpeg(filename)
        
# for filename in os.listdir():
#     if filename.endswith(".png"):
#         shutil.move(file_source + filename, file_destination + filename)
# convert2jpeg('11АТ.pdf')

for folder in os.listdir('C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/Детское/'):
    print(folder)
    path = f'C:/Users/k8909/OneDrive/Документы/GitHub/learning-Python/for_me/Детское/{folder}/'
    os.mkdir(f"{path}photo")
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