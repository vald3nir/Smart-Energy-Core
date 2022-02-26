import uuid

import qrcode


def create_device_qrcode():
    device = uuid.uuid1()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(device)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'src/devices/{device}.png')



