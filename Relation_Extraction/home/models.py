from django.db import models

class Object(models.Model):
    object_1 = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    object_2 = models.CharField(max_length=100)

    def __str__(self):
        return self.object_1 + ": " + self.relation + ": " + self.object_2
