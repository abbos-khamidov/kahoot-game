from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'),(3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return self.text