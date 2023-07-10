import qrcode
def get_qr(text,filename,fill='black',color = 'white'):
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color=fill,back_color=color)
    img.save(filename)