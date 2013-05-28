from django.db import models
from django.utils import timezone
import os

#unique name for upload file
import uuid
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('pictures/', filename)

class Picture(models.Model):
    image = models.ImageField(upload_to=get_file_path)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    picture = models.ForeignKey(Picture)
    author = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __unicode__(self):
        return self.description
