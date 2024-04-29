from django.db import models


class PersonalInformation(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    birthdate = models.DateField()

