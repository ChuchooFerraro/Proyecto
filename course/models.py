from django.db import models
from ckeditor.fields import RichTextField

class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    description = RichTextField(blank = True, null=True)


    def __str__(self):
        return f'{self.name} course --'