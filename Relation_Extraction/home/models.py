from django.db import models

class Object(models.Model):
    object_1 = models.CharField(max_length=500)
    object_1_type = models.CharField(max_length=500)
    relation = models.CharField(max_length=500)
    object_2 = models.CharField(max_length=500)
    object_2_type = models.CharField(max_length=500)
