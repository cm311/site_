from django.contrib import admin
from .models import Post, Tag, WH3Lord
from .forms import PostForm


class PostAdmin(admin.ModelAdmin):
    form = PostForm

#set so that we can see the id field in the admin
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(WH3Lord)

