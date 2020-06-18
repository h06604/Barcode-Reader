
 
import cv2
import pyzbar.pyzbar as pyzbar
import time
import os

def decodeDisplay(image,lastbarcodeData):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        if barcodeData != lastbarcodeData:
            lastbarcodeData = barcodeData
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,barcodeData)
            os.system("beep -f 555 -l 460")
            fo = open("test.txt", "r+")
            fo.seek(0, 2)
            fo.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' '+ barcodeData + '\n' )
    return (image,lastbarcodeData)
 
 
def detect():
 
    camera = cv2.VideoCapture(0)
    checkstring = ""

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (im,checkstring)=decodeDisplay(gray,checkstring)
        cv2.waitKey(5)
        cv2.imshow("camera", im)
 
    camera.release()
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    detect()
