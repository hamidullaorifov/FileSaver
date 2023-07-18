from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='files')


    @property
    def url(self):
        try:
            return self.file.url
        except:
            return ''
