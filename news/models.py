from django.db import models

# Create your models here.
class news(models.Model):
    title=models.CharField(max_length=50,null=True)
    details=models.TextField(max_length=500,null=True)
    occurenceDate=models.DateTimeField(max_length=50,null=True)
    image = models.FileField(max_length=200,null=True)
    


    def  __str__(self):
        return self.title
