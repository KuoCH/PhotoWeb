from django.db import models
from django.utils import timezone
import os
from django import forms

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

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

#Delete file when model delete
@receiver(pre_delete, sender=Picture)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%m/%d/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        field = ['image', 'title', 'description']
