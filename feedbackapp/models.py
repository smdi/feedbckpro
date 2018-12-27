from django.db import models

# Create your models here.



class FeedbackData(models.Model):
    name = models.CharField(max_length= 20)
    rating = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=2000)







