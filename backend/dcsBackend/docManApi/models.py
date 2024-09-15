from django.db import models

# Create your models here.
class document(models.Model):
    document_id = models.IntegerField()
    document_name = models.CharField(max_length=10)
    document_type = models.CharField(max_length=10)
