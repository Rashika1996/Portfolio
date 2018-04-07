from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/') # upload to specifies what should be the location where u need to upload images  
    summary = models.CharField(max_length=200)
