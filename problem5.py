#!/usr/bin/python -tt
# coding: utf-8

# Author Qunzhao
# 2106/8/18

import Image
import sys
import os
import re

def imgresize(srcfilename):
  """
  Resize image to make sure Image Height <= 1136 and Image Width <= 640
  """
  #Open image and get image size
  #print srcfilename
  im = Image.open(srcfilename)
  #print im.mode, im.size, im.format
  (imwidth, imheight) = im.size
  
  #Rsize image
  height_ratio = (imheight + 0.0)/1136
  width_ratio = (imwidth + 0.0)/640
  #print height_ratio, width_ratio

  if (height_ratio > 1.0) or (width_ratio > 1.0):
    if height_ratio >= width_ratio:
      new_height = imheight/height_ratio
      new_width = imwidth/height_ratio
    else:
      new_height = imheight/width_ratio
      new_width = imwidth/width_ratio

    #print new_height, new_width

    im = im.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
    old_basename = os.path.basename(srcfilename)
    old_dir = os.path.dirname(srcfilename)
    new_dir = old_dir+'/resizedimg'
    if not os.path.exists(new_dir):
      os.mkdir(new_dir)
    new_basename = 'resized_' + old_basename
    newfilename = os.path.join(new_dir, new_basename)
    im.save(newfilename)
  
def main():
  if len(sys.argv) != 2:
    print 'usage: ./reshape_img.py imgdir'
    sys.exit(1)

  imgdir = sys.argv[1]
  flist = os.listdir(imgdir)
  
  for f in flist:
    #print f
    fmatch = re.search(r'\w+\.(jpg|jpeg|png|tiff|bmp)$', f) 
    if fmatch:
      #print 'MATCH: %s' % f
      filepath = os.path.join(imgdir, f)
      abspath = os.path.abspath(filepath)
      imgresize(abspath)


if __name__ == '__main__':
  main()
