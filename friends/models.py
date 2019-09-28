from django.db import models

class Person(models.Model):
    first_name = models.CharField('FIRST NAME',max_length=255)
    last_name = models.CharField('LAST NAME',max_length=255)

    def __str__(self):
        return '[' + self.first_name + ']'
