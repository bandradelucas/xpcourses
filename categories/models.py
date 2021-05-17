from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)
    parent = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True)
    image = models.ImageField(null=True, upload_to='uploads/', height_field=None, width_field=None, max_length=100);
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
