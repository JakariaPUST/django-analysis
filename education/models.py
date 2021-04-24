from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.name
