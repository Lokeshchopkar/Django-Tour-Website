from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=500, default="")
    conheading = models.CharField(max_length=500,default="")
    subheading1 = models.CharField(max_length=500, default="")
    consubheading1 = models.CharField(max_length=5000, default="")
    subheading2 = models.CharField(max_length=500, default="")
    consubheading2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="tourpackage/images", default="")

    def __str__(self):
        return self.title