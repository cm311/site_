from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Post, Tag, WH3Lord
from .forms import PostForm


class PostAdmin(admin.ModelAdmin):
    form = PostForm

#set so that we can see the id field in the admin
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class WH3LordAdmin(admin.ModelAdmin):
    formfield_overrides =  {
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80, 'style': 'font-family: monospace; white-space: pre;'})},
    }


# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(WH3Lord, WH3LordAdmin)

