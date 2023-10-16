import cv2 as cv
import numpy as np



def setbit (a,strin,i,c):
    if strin[i] == '1':
        a[c // cols, c % cols] |= 1
    else:
        a[c // cols, c % cols] &= ~1
    return a




#reading and displaying original image
in_img=cv.imread("owl.jpeg")
cv.imshow("input image",in_img)
cv.waitKey(50)


# splitting into bgr mat
b,g,r=cv.split(in_img)

rows=in_img.shape[0]
cols=in_img.shape[1]
maxchar=rows*cols*3/8 -16




str_in=input("input string (max number of characters is %5d): \n" %(maxchar))
messagelen=len(str_in)

while(messagelen>maxchar):
    print("input string too long please enter a shorter string \n")
    str_in=input("input string (max number of characters is %5d): \n" %(maxchar))

#encoding length to front of message
str_in_bin=str(format(messagelen,'016b'))
#sring to binary
str_in_bin =str_in_bin+ ''.join(format(ord(i), '08b') for i in str_in)
print("The Binary value after string conversion is:",str_in_bin)

#encoding in bgr values
for i in range(len(str_in_bin)):
    if(i%3==0):
        b=setbit(b,str_in_bin,i,i//3)
    if(i%3==1):
        g=setbit(g,str_in_bin,i,(i-1)//3)
    if(i%3==2):
        r=setbit(r,str_in_bin,i,(i-2)//3)

#display and save images
out_img=cv.merge([b,g,r])
cv.imwrite("C:\LSBSteganography\output_image.png",out_img)
cv.imshow("output image",out_img)
cv.waitKey(0)
cv.destroyAllWindows()
