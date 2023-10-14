import cv2 as cv
import numpy as np
oimg=cv.imread("owl.jpeg")

#reading image & displaying original image
#cv.imshow("oops",oimg)
# cv.waitKey(0)


# splitting into bgr mat
b,g,r=cv.split(oimg)

#sring to binary
str_in=input("input string")
str_in_bin = ''.join(format(ord(i), '08b') for i in str_in)



#binary to string
str_out =' '

for i in range(0, len(str_in_bin), 8):

    temp_data = str_in_bin[i:i + 8]
    decimal_data = int(temp_data,2)
    str_out = str_out + chr(decimal_data) 
 
print("The Binary value after string conversion is:",
       str_out)




#convert asci to binary
#split bitwise

#set image bits
#display moded image
#input image
#store last bits of image
#convert to ascii



#how to know when the message ends??
#display space available
#possible security login



cv.waitKey(0)
