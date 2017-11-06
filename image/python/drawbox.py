# -*-coding:utf8-*-
# vim: set et:ts=4:sw=4
#


# pyinstaller --onefile -c
#    : 경로에 한글이 오면 안됨
#    : python3 환경에서 작업할 것.  python2는 pyinstaller로 만든 exe가 PIL import error를 발생
#
# 실행예 : drawbox.exe "D:\TestImage.jpg" 381,612,642,686 513,630,540,670 544,629,567,670 570,629,595,669 601,628,625,669
# 출력 : out.png 파일 생성

# https://stackoverflow.com/questions/34255938/is-there-a-way-to-specify-the-width-of-a-rectangle-in-pil

from PIL import Image, ImageDraw, ImageFont
import sys

# draw rectangle thickness 2px
def draw_rectangle(rect, color):
    # 1st pixel box
    draw.rectangle(rect, outline=color)
    
    # 2nd pixel box
    rect_start = (rect[0]-1 , rect[1]-1)
    rect_end = (rect[2]+1 , rect[3]+1)
    draw.rectangle((rect_start, rect_end), outline=color)

if __name__ == "__main__":
    imgfile = sys.argv[1] # image file
    bx_plate = sys.argv[2]  # 번호판 좌표
    bx4 = (sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])  # 숫자 4자리 좌표
    
    im  = Image.open(imgfile).convert('RGBA')
    draw = ImageDraw.Draw(im)
    
    # string to tuple : eval('2,3,4') becomes (2,3,4)
    draw_rectangle(eval(bx_plate) , "#ff2200")
    
    for b in bx4:
        draw_rectangle(eval(b) , "#00ff22")
    
    del draw
    #im.show()  # show image with system image viewer
    # http://pillow.readthedocs.io/en/3.4.x/handbook/image-file-formats.html#png
    # compress_level : 1 gives best speed
    im.save("out.png", "PNG" , compress_level=1)
