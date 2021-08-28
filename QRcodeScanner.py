import qrcode                  # pip install qrcode
import cv2                     # pip install opencv-python

def generator():
    text= "sovon"              #input()   akhane j ta QR code banabi seta link kor
    code_name=  "sovonQr"         #input()  akhane j name hobe seta user ar theke chaite hobe
    img = qrcode.make(text)

    img.save(code_name+".jpg")         



def scanner():
    d=cv2.QRCodeDetector()
    image= "123.jpg" # akhane image input ne

    val, points, straight_qrcode = d.detectAndDecode(cv2.imread("123.jpg"))         # akhane akta image input niye  oi  image tar jayga te bosate hobe

    print(val)


if __name__ == '__main__':


    #generator()
    #scanner()