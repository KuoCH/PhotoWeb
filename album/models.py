from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to="pictures/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

class Comment(models.Model):
    picture = models.ForeignKey(Picture)
    author = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
