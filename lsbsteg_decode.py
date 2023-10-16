import cv2 as cv
import numpy as np
#read image and display
in_img=cv.imread("output_image.png")
cv.imshow("input image",in_img)
cv.waitKey(0)
cv.destroyAllWindows()
#cant teill if it work xd

b,g,r=cv.split(in_img)

rows=in_img.shape[0]
cols=in_img.shape[1]
strlen=''
for i in range(0,4):
    if b[i // cols, i % cols] %2 == 1:
        strlen=strlen+'1'
    else:
        strlen=strlen+'0'

    if g[i // cols, i % cols] %2 == 1:
        strlen=strlen+'1'
    else:
        strlen=strlen+'0'

    if r[i // cols, i % cols] %2 == 1:
        strlen=strlen+'1'
    else:
        strlen=strlen+'0'
n=int(strlen,2)
print(n)


str_out_bin=''
for i in range(0,n):
    if b[i // cols, i % cols] %2 == 1:
        str_out_bin=str_out_bin+'1'
    else:
        str_out_bin=str_out_bin+'0'

    if g[i // cols, i % cols] %2 == 1:
        str_out_bin=str_out_bin+'1'
    else:
        str_out_bin=str_out_bin+'0'

    if r[i // cols, i % cols] %2 == 1:
        str_out_bin=str_out_bin+'1'
    else:
        str_out_bin=str_out_bin+'0'

#binary to string
str_out =' '

for i in range(0, len(strlen), 8):

    temp_data = strlen[i:i + 8]
    decimal_data = int(temp_data,2)
    str_out = str_out + chr(decimal_data) 
 
print("The Binary value after string conversion is:",
       str_out)
