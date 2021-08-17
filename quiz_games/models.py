from django.db import models

class CommonInfo(models.Model):
    difficulty = models.CharField(max_length=6)
    category = models.CharField(max_length=60)
    type = models.CharField(max_length=15)

    class Meta:
        abstract = True
    
class Question(CommonInfo):
    question = models.CharField(max_length=550)
    correct_answer = models.CharField(max_length=50)
    incorrect_answer_one = models.CharField(max_length=50)
    incorrect_answer_two = models.CharField(max_length=50)
    incorrect_answer_three = models.CharField(max_length=50) 

    def __str__(self):
        return self.question