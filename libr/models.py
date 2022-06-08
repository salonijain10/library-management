from django.db import models

# Create your models here.
class dbadmin(models.Model):
    email= models.EmailField(max_length=30, unique=True)
    password= models.CharField(max_length=20)

    def __str__(self):
        return self.email

    empAuth_objects = models.Manager()

class bookdb(models.Model):
    bname= models.CharField(max_length=30, unique=True)
    author = models.CharField(max_length=30)
    isbn = models.IntegerField()
    category=models.CharField(max_length=30)

    def __str__(self):
        return self.bname

    empBook_objects = models.Manager()

