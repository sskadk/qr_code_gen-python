'''
--->  Important Note:                                  <---
--->  Before running this program:                     <---
--->  QR Module and Image Module should be installed.  <---
'''



import qrcode                       # -->  Importing QR Module
from PIL import Image               # -->  Importing PIL from Image Module  
data=input("Enter Data of which you want to make QrCode:")
qrname=input("Enter your QrCode Name:")
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=4,)
qr.add_data(f"{data}")
qr.make(fit=True)
img=qr.make_image(fill_color="white", back_color="black")
img.save(f"{qrname}.png")

'''
End of Program and is Just Simple
'''
