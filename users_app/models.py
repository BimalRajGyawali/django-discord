from django.db import models



class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.email} {self.roll}'


