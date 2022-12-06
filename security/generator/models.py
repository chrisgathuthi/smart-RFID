from email.policy import default
from django.db import models
from django.db.models import Q
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):    
    """
    students model for database
    """
    os_list= (("windows","Windows"),("harmony","harmony"),("ubuntu","ubuntu"),("ios","ios"),("android","android"),("linux","linux"))
    qr_code = models.ImageField(upload_to="QR",help_text="student image",blank=True,editable=False)
    first_name = models.CharField(max_length=19,help_text="student first name")
    last_name = models.CharField(max_length=19,help_text="student last name")
    email = models.EmailField(help_text="student email")
    reg_no = models.CharField(max_length=16,help_text="registration number ")
    gadget_brand = models.CharField(max_length=15,help_text="e.g. hp")
    gadget_model = models.CharField(max_length=15,help_text="folio 9470")
    gadget_serial = models.CharField(max_length=15,help_text="CNU4149***")
    gadget_os = models.CharField(max_length=8,choices=os_list)
    reg_date= models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.reg_no}"







