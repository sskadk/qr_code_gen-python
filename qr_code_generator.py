'''
Note: Before running this program 
QR Module and Image Module
should be installed

'''
import qrcode           #QR Module
from PIL import Image   #Image Module  
data=input("Enter Data of which you want to make QrCode:")
qrname=input("Enter your QrCode Name:")
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=4,)
qr.add_data(f"{data}")
qr.make(fit=True)
<<<<<<< HEAD
img=qr.make_image(fill_color="white", back_color="black")
img.save(f"{qrname}.png")
=======
img=qr.make_image(fill_color="red", back_color="blue")
img.save("NewQr.png")

#Too_Simple
>>>>>>> 64a296174cfb839ded6223233aa691d9d929efb9
