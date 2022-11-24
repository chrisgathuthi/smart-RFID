import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

#img = cv.imread(r"C:\Users\HP\Documents\Dev\Pyscripts\opencv\qrcode-hdb212-0351-2019.png")
cap = cv.VideoCapture(0,cv.CAP_DSHOW)

cap.set(3,640)
cap.set(4,640)
with open(r"C:\Users\HP\Documents\Dev\smart-RFID\security\db_data.txt","r") as f:
    datalist = f.read().splitlines()
print(datalist)
while False:
    success,img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode("utf-8")
        print(myData)
        if myData in datalist:
            myoutput = "Valid QR"
            colors = (0,255,0)
        else:
            myoutput = "Invalid QR"
            colors = (0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv.putText(img,myoutput,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,colors,2)

        cv.imshow("Results",img)
        cv.waitKey(1)


