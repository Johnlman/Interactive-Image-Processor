import cmpt120imageHelper
img=cmpt120imageHelper.getImage("fish.jpg")
imgcopy=cmpt120imageHelper.getImage("fish.jpg")
height=len(img)
width=len(img[0])
black=cmpt120imageHelper.getBlackImage(width,height)
def coverRightHalf(pixels):
  for row in range(height):
    for col in range(width):
      if col >= int(width/2):
        pixels[row][col]=black[row][col]
  cmpt120imageHelper.showImage(pixels)
  return pixels
def swapRedwithBlue(pixels):
  for row in range(height):
    for col in range(width):
      r=img[row][col][0]
      b=img[row][col][2]
      pixels[row][col][0]=b
      pixels[row][col][2]=r
  cmpt120imageHelper.showImage(pixels)
  return pixels
def flipVerticle(pixels):
  for row in range(height):
    for col in range(width):
        pixels[row][col]=imgcopy[height-1-row][col]
  cmpt120imageHelper.showImage(pixels)
  return pixels
def invert(pixels):
  for row in range(height):
    for col in range(width):
      r=pixels[row][col][0]
      g=pixels[row][col][1]
      b=pixels[row][col][2]
      pixels[row][col][0]=255-r
      pixels[row][col][1]=255-g
      pixels[row][col][2]=255-b
  cmpt120imageHelper.showImage(pixels)
  return pixels
def grayscale(pixels):
  for row in range(height):
    for col in range(width):
      r=pixels[row][col][0]
      g=pixels[row][col][1]
      b=pixels[row][col][2]
      gray=(r+b+g)/3
      pixels[row][col][0]=gray
      pixels[row][col][1]=gray
      pixels[row][col][2]=gray
  cmpt120imageHelper.showImage(pixels)
  return pixels
def RedFilter(pixels):
  for row in range(height):
    for col in range(width):
      pixels[row][col][1]=0
      pixels[row][col][2]=0
  cmpt120imageHelper.showImage(pixels)
  return pixels
def GreenFilter(pixels):
  for row in range(height):
    for col in range(width):
      pixels[row][col][0]=0
      pixels[row][col][2]=0
  cmpt120imageHelper.showImage(pixels)
  return pixels
def BlueFilter(pixels):
  for row in range(height):
    for col in range(width):
      pixels[row][col][0]=0
      pixels[row][col][1]=0
  cmpt120imageHelper.showImage(pixels)
  return pixels
def SepiaFilter(pixels):
  for row in range(height):
    for col in range(width):
      r=img[row][col][0]
      g=img[row][col][1]
      b=img[row][col][2]
      SepiaRed=int(r*0.393)+int(g*0.769)+int(b*0.189)
      SepiaGreen=int(r*0.349)+int(g*0.686)+int(b*0.168)
      SepiaBlue=int(r*0.272)+int(g*0.534)+int(b*0.131)
      if SepiaRed>255:
        pixels[row][col][0]=255
      else:
        pixels[row][col][0]=SepiaRed
      if SepiaGreen>255:
        pixels[row][col][1]=255    
      else:
        pixels[row][col][1]=SepiaGreen
      if SepiaBlue>255:
        pixels[row][col][2]=255  
      else:
        pixels[row][col][2]=SepiaBlue
  cmpt120imageHelper.showImage(pixels)
  return pixels
def WarmFilter(pixels):
  for row in range(height):
    for col in range(width):
      if pixels[row][col][0]<64:
        pixels[row][col][0]=int((pixels[row][col][0]/64)*80)
      elif pixels[row][col][0]>=64 and pixels[row][col][0]<128:
        pixels[row][col][0]=int(((pixels[row][col][0]-64)/(128-64))*(160-80)+80)
      else:
        pixels[row][col][0]=int(((pixels[row][col][0]-128)/(255-128))*(255-160)+160)
      if pixels[row][col][2]<64:
        pixels[row][col][2]=int((pixels[row][col][2]/64)*50)
      elif pixels[row][col][2]>=64 and pixels[row][col][2]<128:
        pixels[row][col][2]=int(((pixels[row][col][2]-64)/(128-64))*(100-50)+50)
      else:
        pixels[row][col][2]=int(((pixels[row][col][2]-128)/(255-128))*(255-100)+100)
      
  cmpt120imageHelper.showImage(pixels)
  return pixels
def ColdFilter(pixels):
  for row in range(height):
    for col in range(width):
      if pixels[row][col][2]<64:
        pixels[row][col][2]=int((pixels[row][col][2]/64)*80)
      elif pixels[row][col][2]>=64 and pixels[row][col][2]<128:
        pixels[row][col][2]=int(((pixels[row][col][2]-64)/(128-64))*(160-80)+80)
      else:
        pixels[row][col][2]=int(((pixels[row][col][2]-128)/(255-128))*(255-160)+160)
      if pixels[row][col][0]<64:
        pixels[row][col][0]=int((pixels[row][col][0]/64)*50)
      elif pixels[row][col][0]>=64 and pixels[row][col][0]<128:
        pixels[row][col][0]=int(((pixels[row][col][0]-64)/(128-64))*(100-50)+50)
      else:
        pixels[row][col][0]=int(((pixels[row][col][0]-128)/(255-128))*(255-100)+100)
  cmpt120imageHelper.showImage(pixels)
  return pixels
def RotateLeft(pixels):
  rotatedimg=cmpt120imageHelper.getBlackImage(height,width)
  for row in range(height):
    for col in range(width):
      rotatedimg[col][row]=pixels[row][width-1-col]
  cmpt120imageHelper.showImage(rotatedimg)
  return rotatedimg
def RotateRight(pixels):
  rotatedimg=cmpt120imageHelper.getBlackImage(height,width)
  for row in range(height):
    for col in range(width):
      rotatedimg[col][row]=pixels[height-1-row][col]
  cmpt120imageHelper.showImage(rotatedimg)
  return rotatedimg
def DoubleSize(pixels):
  newimg=cmpt120imageHelper.getBlackImage(2*width,2*height)
  for row in range(2*height):
    for col in range(2*width):
      newimg[row][col]=pixels[row//2][col//2]
  print(len(newimg))
  print(len(newimg[0]))
  cmpt120imageHelper.showImage(newimg)
  return newimg
def HalfSize(pixels):
  newimg=cmpt120imageHelper.getBlackImage(width//2,height//2)
  for row in range(height//2):
    for col in range(width//2):
      newimg[row][col]=pixels[row*2][col*2]
  print(len(newimg))
  print(len(newimg[0]))
  cmpt120imageHelper.showImage(newimg)
  return newimg

def rgb_to_hsv(r, g, b):
    """
    Input:  r, g, b - the R/G/B values of a pixel in the RGB colour space
    Output: a tuple of the Hue, Saturation, and Value representation of a pixel
    From https://www.w3resource.com/python-exercises/math/python-math-exercise-77.php
    """
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v
def ColourSwap(img):
  newimg=cmpt120imageHelper.getBlackImage(width,height)
  detectedx=[]
  detectedy=[]
  for row in range(height):
    for col in range(width):
      rgb_to_hsv(img[row][col][0],img[row][col][1],img[row][col][2])
      h=rgb_to_hsv(img[row][col][0],img[row][col][1],img[row][col][2])[0]
      s=rgb_to_hsv(img[row][col][0],img[row][col][1],img[row][col][2])[1]
      v=rgb_to_hsv(img[row][col][0],img[row][col][1],img[row][col][2])[2]
      if 1<=h<=100 and 30<=s<=100 and 85<=v<= 100:
        detectedy.append(row)
        detectedx.append(col)
  for r in range(min(detectedx),max(detectedx)+1):
        img[min(detectedy)][r][0]=0
        img[min(detectedy)][r][1]=255
        img[min(detectedy)][r][2]=0
  for r in range(min(detectedx),max(detectedx)+1):
        img[max(detectedy)][r][0]=0
        img[max(detectedy)][r][1]=255
        img[max(detectedy)][r][2]=0
  for c in range(min(detectedy),max(detectedy)+1):
        img[c][min(detectedx)][0]=0
        img[c][min(detectedx)][1]=255
        img[c][min(detectedx)][2]=0
  for c in range(min(detectedy),max(detectedy)+1):
        img[c][max(detectedx)][0]=0
        img[c][max(detectedx)][1]=255
        img[c][max(detectedx)][2]=0
  newimg=img
  cmpt120imageHelper.showImage(newimg)
  return newimg