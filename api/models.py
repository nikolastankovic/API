from django.db import models





class File(models.Model):
    username = models.CharField(max_length=20,blank=False)
    bday  = models.DateField(blank=False)
    file = models.FileField(blank=False, null=False)
       
     
    def __str__(self):
        return self.username