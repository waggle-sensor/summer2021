import cv2
 
# Opens the Video file
cap= cv2.VideoCapture('C:/Users/Owner/.spyder-py3/movieON20191110.mpg')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('Frame'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
