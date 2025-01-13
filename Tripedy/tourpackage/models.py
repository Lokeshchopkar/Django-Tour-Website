from django.db import models

# Create your models here.
class Package(models.Model):
    package_id = models.AutoField
    package_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="tourpackage/images", default="")

    def __str__(self):
        return self.package_name
    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField()
    peraddress = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip = models.IntegerField()
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    inputTraveller = models.CharField(max_length=10)
    amount = models.IntegerField(default=0, null=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    textarea=models.CharField(max_length=1000)
