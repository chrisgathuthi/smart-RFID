from django.db.models.signals import pre_save
from django.dispatch import receiver
import qrcode
from .models import Student



@receiver(pre_save,sender=Student)
def generate_qr(instance,created,sender,**kwargs):
    if created:
        reg = instance.reg_no
        pass




# Importing library
import qrcode

# Data to encode
data = "GeeksforGeeks"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
					back_color = 'white')

img.save('MyQRCode2.png')

