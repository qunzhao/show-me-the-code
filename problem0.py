#!/usr/bin/python -tt
# coding: utf-8

import Image
import ImageDraw
import ImageFont

im = Image.open("qq.jpeg")
print im.mode, im.size, im.format

(imheight, imwidth) = im.size
print imheight, imwidth

draw = ImageDraw.Draw(im)
ttFont = ImageFont.truetype("/usr/share/fonts/turetype/freefont/FreeSansBold.ttf", 30)
draw.text((0.85*imheight, 0.05*imwidth), '4', font=ttFont, fill=(255,0,0))
del draw

im.save('tagqq.jpeg', "JPEG")
