import qrcode
import image

qr = qrcode.QRCode(
    version = 5,#higher the number bigger and complicated the qr image is, acc to me more iterations of blocks are seen in qr code image
    box_size = 5,#defines the size of the box
    border = 1  #gap between the qr code and the white border
)

data = 'I LOVE YOU'#https://www.geeksforgeeks.org/python-programming-language/?ref=shm

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="green")
img.save("qr.png")