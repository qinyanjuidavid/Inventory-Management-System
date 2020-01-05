from django.db import models
from datetime import date

class OperatingSystem(models.Model):
    operating_System=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.operating_System}"

class Computer(models.Model):
    computer_name=models.CharField(max_length=30,blank=True,null=True)
    IP_address=models.CharField(max_length=30,unique=True)
    Mac_address=models.CharField(max_length=30,unique=True)
    Users_name=models.CharField(max_length=30,blank=True,null=True)
    Operating_system=models.ForeignKey(OperatingSystem,on_delete=models.CASCADE)
    location=models.CharField(max_length=30)
    purchase_date=models.DateField("Purchase Date(mm/dd/yy)",blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)


    def __str__(self):
        return f'{self.computer_name} {self.IP_address}'
