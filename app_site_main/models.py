from django.db import models
from django.conf import settings
from django import forms

# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.value

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=False, related_name="posts")

    def __str__(self):
        return self.title

class WH3Lord(models.Model):
    name = models.TextField(max_length=200)
    faction = models.TextField(max_length=100)
    summary_of_changes = models.TextField(max_length=500)

    def __str__(self):
        return str(self.faction) + '_' + str(self.name)
