from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Student
# Create your views here.


class IndexTemplate(TemplateView):
    template_name = "index.html"
   

#htmx views
class FormData(View):
    def get(self,request,*args,**kwargs):
        data = request.GET.get("reg","")
        qs = Student.objects.filter(reg_no__iexact=data)
        return render(request,"results.html",{"qs":qs})