'''
Note: Before running this program 
QR Module and Image Module
should be installed

'''
import qrcode           #QR Module
from PIL import Image   #Image Module  

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=4,)
qr.add_data("Enter your data to make a QR")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="blue")
img.save("NewQr.png")