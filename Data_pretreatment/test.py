# 텍스트를 이미지로 만들어서 훈련 데이터로 사용하기 위한 목적
from PIL import Image,ImageDraw,ImageFont

# 이미지로 출력할 글자 및 폰트 지정 
draw_text = '가'
font_size = 90
font = ImageFont.truetype("../FONT_GENERATOR/data/font/sorce/sorce.ttf", font_size)
 
# 이미지 사이즈 지정
text_width = 125
text_height = 125
 
# 이미지 객체 생성 (배경 white)
canvas = Image.new('RGB', (text_width, text_height), "white")
 
# 가운데에 그리기 (폰트 색: black)
draw = ImageDraw.Draw(canvas)
w, h = font.getsize(draw_text)
draw.text(((text_width-w)/2.0,(text_height-h)/2.0), draw_text, 'black', font)
 
# 가.png로 저장 및 출력해서 보기
canvas.save(draw_text+'.png', "PNG")
canvas.show()
