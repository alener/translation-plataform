from django.db import models
from django.utils import timezone
from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.

class tradu(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default='')
    origintitle = models.CharField("título original",max_length=40)
    origintext = models.TextField("texto original")
    publicdate = models.DateField("fecha de la publicación",default=timezone.now)
    publilink = models.URLField("link a la publicación",null= True, blank=True)
    transtitle = models.CharField("título traducido",max_length=40)
    transtext = models.TextField("texto traducido")
    transdate = models.DateTimeField("comienzo de la traducción",auto_now_add=True, )
    transupdate = models.DateTimeField("última actualización de la traducción",default=timezone.now)
    translink = models.URLField("link a la traducción",null=True, blank=True)
    content = HTMLField(default='')


    def __str__(self):
        return self.transtitle

    class META:
        verbose_name='traducción'
        verbose_name_plural="traducciones"

