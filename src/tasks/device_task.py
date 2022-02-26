import uuid

import qrcode


def create_device_qrcode(user):
    device_id = uuid.uuid1()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(device_id)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'src/devices/{user}-{device_id}.png')
    return f'{device_id}'


def create_new_user_with_device(users):
    for user in users:
        print({"user": user, "device": create_device_qrcode(user)})
