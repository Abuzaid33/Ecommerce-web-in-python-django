from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=150)


class sun_category(models.Model):
    name = models.CharField(max_length=150)
    category - models.ForeignKey(category,  on_delete=models.CASCADE)






