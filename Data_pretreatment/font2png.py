'''This code is the code that creates data for font learning in GAN machine learning. 
In this code, one source font text and one target font text are output to a canvas 
of 250*125 size and output as a png file. '''

'''이 코드는 GAN 머신러닝에서 글꼴 학습을 위한 데이터를 생성하는 코드입니다.
이 코드에서 하나의 소스 글꼴 텍스트와 하나의 대상 글꼴 텍스트가 캔버스에 출력됩니다.
250*125 크기의 캔버스에 글자들이 png 파일로 출력됩니다. '''

from PIL import Image,ImageDraw,ImageFont
import os
import numpy as np
import random

#글꼴 출력하는 함수
def write(target_font, sorce_font, draw_text):

    #폰트 사이즈 & 폰트 종류 지정
    font_size = 90
    s_font = ImageFont.truetype("../FONT_GENERATOR/data/font/sorce/" + str(sorce_font), font_size)
    t_font = ImageFont.truetype("../FONT_GENERATOR/data/font/target/" + str(target_font), font_size)

    # 이미지 사이즈 지정
    text_width = 250
    text_height = 125
 
    # 이미지 객체 생성 (배경 white)
    canvas = Image.new('RGB', (text_width, text_height), "white")
 
    # 가운데에 그리기 (폰트 색: black)
    draw = ImageDraw.Draw(canvas)
    w1, h1 = s_font.getsize(draw_text)
    draw.text(((text_width/2-w1)/2.0,(text_height-h1)/2.0), draw_text, 'black', s_font)

    w2, h2 = t_font.getsize(draw_text)
    draw.text(((text_width/2-w2)/2.0+125, (text_height-h2)/2.0), draw_text, 'black', t_font)

    #저장하기
    canvas.save(target_font+draw_text+'.png', "PNG")

#소스 폰트 지정
sorce_font = "sorce.ttf"
sorce_font_path = "../FONT_GENERATOR/data/font/sorce/" + str(sorce_font)

for i in range(1, 31):
    #타켓 폰트 지정
    target_font= "target"+str(i)+".ttf"
    target_font_path= "../FONT_GENERATOR/data/font/target/" + str(target_font)

    #한 폰트에서 3000개의 임의의 한글 글자를 추출할 예정
    random
    for j in range():
        #임의의 한글 지정
        draw_text = ""

        #write 함수로 텍스트 png 파일로 만들기
        write(target_font, sorce_font, draw_text)

