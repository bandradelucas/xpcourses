from django.db.models.deletion import DO_NOTHING
from categories.models import Category
from django.db import models
from ckeditor.fields import RichTextField

class Skill(models.Model):
    name = models.CharField(max_length=40);
    image = models.ImageField(null=True, upload_to='media', height_field=None, width_field=None, max_length=100);
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='skills');
    video = models.CharField(blank = True, max_length=255, null=True);
    content = RichTextField(blank = True, null=True);
    xp = models.IntegerField(default=0);
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);

    def __str__(self):
        return self.name