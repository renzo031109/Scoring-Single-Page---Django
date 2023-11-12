from django.db import models

class Score(models.Model):
    name = models.CharField(max_length=100)
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-value']
