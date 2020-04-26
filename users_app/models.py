from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    semester = models.IntegerField(validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f'{self.name} {self.email} {self.roll}'


