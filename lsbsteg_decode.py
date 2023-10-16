import cv2 as cv
import numpy as np

def pixv2bin(b,strl,c):
    if b[c // cols, c % cols] %2 == 1:
        strl=strl+'1'
    else:
        strl=strl+'0'
    return strl

#read image and display
in_img=cv.imread("output_image.png")
cv.imshow("input image",in_img)
cv.waitKey(0)
#cant teill if it work xd

b,g,r=cv.split(in_img)

rows=in_img.shape[0]
cols=in_img.shape[1]
strlen=' '
for i in range(0,16):
    if(i%3==0):
        strlen=pixv2bin(b,strlen,i//3)
    if(i%3==1):
        strlen=pixv2bin(g,strlen,(i-1)//3)
    if(i%3==2):
        strlen=pixv2bin(r,strlen,(i-2)//3)

n=int(strlen,2)


str_out_bin=''
for i in range(16,16+n*8):
    if(i%3==0):
        str_out_bin=pixv2bin(b,str_out_bin,i//3)
    if(i%3==1):
        str_out_bin=pixv2bin(g,str_out_bin,(i-1)//3)
    if(i%3==2):
        str_out_bin=pixv2bin(r,str_out_bin,(i-2)//3)
print(str_out_bin)


#binary to string
str_out =''

for i in range(0, len(str_out_bin), 8):

    temp_data = str_out_bin[i:i + 8]
    decimal_data = int(temp_data,2)
    str_out = str_out + chr(decimal_data) 
 
print("The Binary value after string conversion is:\n",str_out)
