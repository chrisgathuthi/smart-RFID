from django.db import models
from django.db.models import Q
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File
# Create your models here.

class StudentManager(models.Manager):
    def search(self,data=None,*args,**kwargs):
        if data is None or data == "":
            return self.get_queryset().none()
        return self.get_queryset().filter(reg_no__iexact=data)


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

    objects =  StudentManager()

    def __str__(self) -> str:
        return f"{self.reg_no}"

    def save(self, *args, **kwargs):
        data = self.reg_no +" "+ self.gadget_serial 
        qrcode_img = qrcode.make(data)
        canvas = Image.new("RGB",(290,290),"white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        new_name = self.reg_no.replace("/","-")
        fname = f"qrcode-{new_name}.png"
        buffer = BytesIO()
        canvas.save(buffer,"Png")
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)



