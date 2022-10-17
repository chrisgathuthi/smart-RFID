from typing import Any, Optional
from django.core.management import BaseCommand
from generator.models import Student

import random


class Command(BaseCommand):
    help = "populating the database"
    def handle(self, *args: Any, **options: Any) -> Optional[str]:

        os_ = ["windows","harmony","ubuntu","ios","android","linux"]
        brands = ["mac","hp","lenovo","asus"]
        for i in range(30):
            Student.objects.create(gadget_os = random.choice(os_),first_name = "jane",last_name = "john",gadget_serial = "hdds333GG",gadget_brand = "folio",gadget_model = random.choice(brands),reg_no = "hdb212-0999/2019",email = "chris@gmail.com")
        print("completed")            
        