from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random

from faker import Faker

from generator.models import Student

class Command(BaseCommand):
    help = "populating the db"

    def handle(self, *args, **options):
        OS_LIST=["windows", "harmony", "ubuntu", "ios", "android", "linux"]
        BRANDS = ["lenovo", "mac book", "hp", "asus", "taifa", "dell", "sumsung", "ryzen"]
        MODEL = ["notebook", "chromebooks", "folio", "M1", "vision"]
        REG = ["1001","2324","2344","6543","2351","2445","1343","6345","4311","7579"]

        for i in range(6):
            NAME = Faker()
            num = random.choice(REG)
            Student.objects.create(
                first_name = NAME.name(),
                last_name = NAME.name(),
                email = NAME.name()+".students@jkuat.ac.ke".replace("","-").lower(),
                reg_no = f"hdb212-{num}/2019",
                gadget_brand = random.choice(BRANDS),
                gadget_model = random.choice(MODEL),
                gadget_serial = get_random_string(10),
                gadget_os = random.choice(OS_LIST),
            ).save()
            random.shuffle(REG)
        self.stdout.write("The process is complete")