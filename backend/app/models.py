from django.db import models

# Create your models here.


class Form(models.Model):
    name = models.CharField(max_length=64)
    dob = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    mobile = models.CharField(max_length=64)
    govt_type = models.CharField(max_length=64)
    id_num = models.CharField(max_length=64)
    guardian_title = models.CharField(max_length=64)
    guardian_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    emer_contact = models.CharField(max_length=64)
    address = models.TextField()
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    pincode = models.CharField(max_length=64)
    occupation = models.CharField(max_length=64)
    religion = models.CharField(max_length=64)
    marital = models.CharField(max_length=64)
    blood = models.CharField(max_length=64)
    nationality = models.CharField(max_length=64)
