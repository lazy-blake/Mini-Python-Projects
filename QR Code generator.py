import qrcode


url = input("Enter your text or url: ").strip()  #to remove any white spaces the user typees
save = input("Enter file name:")

qr = qrcode.QRCode(version=1,box_size=10,border=4)

qr.add_data(url)

qr.make()

img = qr.make_image(fill_color="white",back_color = "black")

img.save(save)




