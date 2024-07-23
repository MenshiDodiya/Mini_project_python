# QR code generator in advance changing the color of QR
# code and background color changing size of box modifies

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4,)
qr.add_data("www.linkedin.com/in/menshi-parmar-mp1310")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save(" linkdin.png ")