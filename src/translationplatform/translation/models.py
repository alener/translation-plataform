from django.db import models

# Create your models here.

class tradu(models.Model):
    origintitle = models.CharField(max_length=40)
    origintext = models.TextField()
    publicdate = models.DateField(default=True)
    transtitle = models.CharField(max_length=40)
    transtext = models.TextField()
    transdate = models.DateTimeField(auto_now=True,)


    def __str__(self):
        return self.transtitle
