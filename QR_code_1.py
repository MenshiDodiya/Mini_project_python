#QR code Generator

import qrcode as qr
img = qr.make("https://www.canva.com")
img.save("canva.png")