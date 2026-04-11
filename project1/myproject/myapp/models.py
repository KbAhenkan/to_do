from django.db import models

# Create your models here.
class ListModel(models.Model):
    Title = models.CharField(max_length=100, primary_key=True)
    Description = models.CharField()
    Due_date = models.DateField()

    def __str__(self):
        return f" {self.Title} is Due: {self.Due_date}" 
    