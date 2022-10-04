
from statistics import mode
from django.db import models

# Create your models here.


def folder(instance,filename):
    return f"codes/{instance.reg_no}/{filename}".format(instance,filename)
class Student(models.Model):
    
    name = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=14)
    serial_no = models.CharField(max_length=20)
    device_brand = models.CharField(max_length=40)
    email = models.EmailField()
    qr_code = models.ImageField(upload_to=folder,editable=False,null=True,blank=True)
    

    def __str__(self) -> str:
        return f"{self.name}"


