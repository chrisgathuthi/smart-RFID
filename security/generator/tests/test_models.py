
from django.test import TestCase
from model_bakery import baker


from generator.models import Student


# Create your tests here.
class TestStaff(TestCase):
    def setUp(self):
        self.chris = baker.make(Student,reg_no="hdb212-0351/2019")
        
        
    def test_model_str(self):
        self.assertEqual(str(self.chris),"hdb212-0351/2019")
    
    def test_form_data(self):
        data= {
            "reg_no":"hdb212-0351/2019"
        }
        response = self.client.get("form-data",data=data)
        r= Student.objects.get(reg_no=data["reg_no"])
        self.assertEqual(str(r),data["reg_no"])
        self.assertEqual(response.status_code,404)
        # self.assertTemplateUsed(response,template_name="index.html")
        


