from django.db import models
class Users(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=200)
    department = models.CharField(max_length=300)
    image = models.ImageField(upload_to='img/%m/%d')

    def __str__(self):
        return self.name