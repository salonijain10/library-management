from django.db import models

class stuDB(models.Model):
    fname= models.CharField(max_length=30)
    lname= models.CharField(max_length=30)
    sid= models.CharField(max_length=20,unique=True)
    password= models.CharField(max_length=20)

    def __str__(self):
        return self.sid

    empAuth_objects = models.Manager()
