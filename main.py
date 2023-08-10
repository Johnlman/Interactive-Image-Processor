#Interactive Image Processor
#John Man
#Nov 11th, 2021
import cmpt120imageHelper
import cmpt120imageManip

img=cmpt120imageHelper.getImage("fish.jpg")
print("Welcome to the Image Processor!\n")
print("Here are your options")
print("0: Quit")
print("1: Cover the right half with black colour")
print("2: Swap all the red components with blue components")
print("3: Flip the image vertically")
print("4: Invert the colour of the image")
print("5: Convert the colour of the image into grayscale")
height=len(img)
width=len(img[0])
User_selection=input("Enter your choice (0/1/2/3/4/5):")
While_Switch=0
while While_Switch==0:
  file_name="result-option"
  file_name+=User_selection+".jpg"
  if User_selection=="0":
    While_Switch=1
    exit()
  elif User_selection=="1":
    cmpt120imageManip.coverRightHalf(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... covering the right half with black colour.")
    print("Image saved as"+ file_name)
    print(len(img))
    print(len(img[0]))
  elif User_selection=="2":
    cmpt120imageManip.swapRedwithBlue(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... Swapping the Red pixels with Blue pixels")
    print("Image saved as"+ file_name)
  elif User_selection=="3":
    cmpt120imageManip.flipVerticle(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... flipping the image vertically.")
    print("Image saved as"+ file_name)
  elif User_selection=="4":
    cmpt120imageManip.invert(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... inverting the colours.")
    print("Image saved as"+ file_name)
  elif User_selection=="5":
    cmpt120imageManip.grayscale(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="6":
    cmpt120imageManip.RedFilter(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="7":
    cmpt120imageManip.GreenFilter(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="8":
    cmpt120imageManip.BlueFilter(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="9":
    cmpt120imageManip.SepiaFilter(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="10":
    cmpt120imageManip.WarmFilter(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="11":
    cmpt120imageManip.ColdFilter(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="12":
    cmpt120imageHelper.saveImage(cmpt120imageManip.RotateLeft(img),file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="13":
    cmpt120imageManip.RotateRight(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="14":
    cmpt120imageManip.DoubleSize(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="15":
    cmpt120imageManip.HalfSize(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  elif User_selection=="16":
    cmpt120imageManip.ColourSwap(img)
    cmpt120imageHelper.saveImage(img,file_name)
    print("OK... replacing all colours with shades of gray")
    print("Image saved as"+ file_name)
  else:
    print("Sorry, I don't understand "+ User_selection)
  User_selection=input("Enter your choice (0/1/2/3/4/5):")
  img=cmpt120imageHelper.getImage("fish.jpg")
input()
