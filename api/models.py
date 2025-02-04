from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return  self.title



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.name



"""

JSON - serializer

  admin
    |
models -> serializer -> views -> urls
"""
