import cv2 as cv
import numpy as np
in_img=cv.imread("owl.jpeg")

#reading image & displaying original image
cv.imshow("input image",in_img)
cv.waitKey(0)


# splitting into bgr mat
b,g,r=cv.split(in_img)

#sring to binary
str_in=input("input string")
str_in_bin = ''.join(format(ord(i), '08b') for i in str_in)
print("The Binary value after string conversion is:",
       str_in_bin)

'''and to set 0, or to set 1 only set lsb'''
col=in_img.shape[1]
#encryption
#will refactor later
for i in range(len(str_in_bin)):
    c=0
    if str_in_bin[c] == '1':
        b[i // col, i % col] |= 1
    else:
        b[i // col, i % col] &= ~1

    if str_in_bin[c+1] == '1':
        g[i // col, i % col] |= 1
    else:
        g[i // col, i % col] &= ~1

    if str_in_bin[c+2] == '1':
        r[i // col, i % col] |= 1
    else:
        r[i // col, i % col] &= ~1
    c+=2

out_img=cv.merge([b,g,r])
cv.imshow("output image",out_img)
cv.waitKey(0)
# #binary to string
# str_out =' '

# for i in range(0, len(str_in_bin), 8):

#     temp_data = str_in_bin[i:i + 8]
#     decimal_data = int(temp_data,2)
#     str_out = str_out + chr(decimal_data) 
 
# print("The Binary value after string conversion is:",
#        str_out)




#display moded image
#input image
#store last bits of image
#convert to ascii



#how to know when the message ends??
#display space available
#possible security login



cv.waitKey(0)
