from django.db import models

class Event(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length = 100)
    def __str__(self):
        return f'{self.title}'
class Registration(models.Model):
    name = models.CharField(max_length = 1000)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete = models.CASCADE)   
    def __str__(self):
        return f'{self.name}'