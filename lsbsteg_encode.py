import cv2 as cv
import numpy as np



def setbit (q,strin,i,c):
    if strin[i] == '1':
        q[c // cols, c % cols] |= 1
    else:
        q[c // cols, c % cols] &= ~1
    return




#reading and displaying original image
in_img=cv.imread("owl.jpeg")
cv.imshow("input image",in_img)
cv.waitKey(0)


# splitting into bgr mat
b,g,r=cv.split(in_img)

rows=in_img.shape[0]
cols=in_img.shape[1]
maxchar=rows*cols*3/8 -16
#sring to binary
str_in=input("input string (max number of characters is %5d): \n" %(maxchar))
messagelen=len(str_in)
str_in_bin=str(format(messagelen,'016b'))
str_in_bin =str_in_bin+ ''.join(format(ord(i), '08b') for i in str_in)
print("The Binary value after string conversion is:",
       str_in_bin)

'''and to set 0, or to set 1 only set lsb'''
#encryption  

for i in range(len(str_in_bin)):
    if(i%3==0):
        setbit(b,str_in_bin,i,i//3)
    if(i%3==1):
        setbit(g,str_in_bin,i,(i-1)//3)
    if(i%3==2):
        setbit(r,str_in_bin,i,(i-2)//3)


out_img=cv.merge([b,g,r])
cv.imwrite("C:\LSBSteganography\output_image.png",out_img)
cv.imshow("output image",out_img)
cv.waitKey(0)
cv.destroyAllWindows()


#how to know when the message ends??
#possible security login