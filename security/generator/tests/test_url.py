from django.test import TestCase

# Create your tests here.
class UrlTest(TestCase):
    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,template_name="index.html")
    
    # def test_form(self):
    #     data= {
    #         "reg_no":"hdb212-0351/2019"
    #     }
    #     response = self.client.get("form-data",data=data)
    #     self.assertEqual(response.status_code,404)
    #     self.assertTemplateUsed(response,template_name="index.html")