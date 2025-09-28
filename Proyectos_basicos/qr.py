"""
    QR basico para un negocio
"""

import qrcode
#importo el generador de la instancia de qr de python
#importo la url para el negocio
url = "https://drive.google.com/file/d/11L7LzgN-8ISVSxF0GLPkAWQfzbmSpqIz/view?usp=sharing"
#ahora solo debo crear el objeto QR
qr = qrcode.make(url)
#guardo la imagen del QR
qr.save("CrissMakeUp_Lista_precios.png")