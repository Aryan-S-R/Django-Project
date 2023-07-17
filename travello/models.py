from django.db import models

# Create your models here.

class Sportsgame(models.Model):
    name = models.CharField(max_length= 100, null = True)
    description = models.CharField(max_length= 100, null = True)
    image = models.ImageField(upload_to="img/other_img", null = True)


    


