from django.db import models

# Create your models here.

class clinicprofile(models.Model):
     id=models.UUIDField( primary_key = True, editable = False)
     name=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     phone=models.CharField(max_length=100)

     class Meta:
         db_table='Clinic'


class Holidays(models.Model):
    date=models.CharField(max_length=50)
    hos_id=models.CharField(max_length=70)
    class Meta:
        db_table='Holidays'

class Weekends(models.Model):
    weekday=models.CharField(max_length=50)
    hos_id=models.CharField(max_length=70)
    class Meta:
        db_table='Weekends'