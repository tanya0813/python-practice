import qrcode 
from PIL import Image  #PIL- helps in formating qrcode

#This creates a custom QRCode object where you decide how the QR will look.
qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,
                 box_size=10,border=4)
#qrcode-taking the data from qrcode,QRcode changes the functionality of qr(border,color, version etc)
#QRcode generally causes error so we use error correction, we are only removing high level error

#You are inserting the data that the QR should contain.
qr.add_data("https://www.youtube.com/@Pranshurockstar") 


#Fit the data properly inside the QR.
qr.make(fit=True)

# This generates the actual QR code image.
img=qr.make_image(fill_color='Red',back_color='blue')

# save the image             
img.save("Pranshu_Rockstar_youtube.png")

