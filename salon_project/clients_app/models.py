from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12)
    last_visit_date = models.DateTimeField()