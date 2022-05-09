from PIL import Image,ImageDraw,ImageFont
import os
import numpy as np

#글꼴 출력하는 함수
def write():
    print()

sorce_font = "sorce.ttf"
sorce_font_path = "../data/sorce/"+str(sorce_font)

for i in range(1, 31):
    target_font= "target"+str(i)+".ttf"
    target_font_path= "../data/target/"+str(target_font)

