import logging
from django.shortcuts import render
from .models import *


#create a module-level logging variable.  Can be used to add logger calls
logger = logging.getLogger(__name__)

# Create your views here.
'''
def index(request):
    return render(request, "app_site_main/index.html")
'''


def index(request, page_number=1):
    #Post object only queried every 300 seconds, all other responses come
    #from cache.  Dont cache stuff whose content relies on logged in user.
    #from django.http import HttpResponse
    #return HttpResponse(str(request.user).encode("ascii"))
    #only load posts that have a publication date in the past

    #when filtering for tags, I Can't just pass a string.  I have to pass the tag id, which for main is 3. (1 on the deployment server)
    #another way to do this is to just filter the tags and get the string from the numbers, but this works too.  I'll just
    # log the tag ids for now.
    posts = Post.objects.filter(tags__in=[1])
    posts = posts.order_by('modified_at').reverse()[(page_number-1) *10 :page_number * 10]

    #get the posts tags
    displayed_posts = {}
    for post in posts:

        #initialize an empty dict for each post, then add the post as ['post'] and the tags as ['tags']
        #custom filters are used to get what is needed from the django templating engine.
        displayed_posts[post.pk] = {}
        displayed_posts[post.pk]['post'] = post
        displayed_posts[post.pk]['tags'] = post.tags.values_list('value', flat=True)

    return render(request, "app_site_main/index.html", {"posts": displayed_posts})

def blog(request, page_number=1):
    posts = Post.objects.all()
    posts = posts.order_by('modified_at').reverse()[(page_number-1) *10 :page_number * 10]

    #get the posts tags
    displayed_posts = {}
    for post in posts:

        #initialize an empty dict for each post, then add the post as ['post'] and the tags as ['tags']
        #custom filters are used to get what is needed from the django templating engine.
        displayed_posts[post.pk] = {}
        displayed_posts[post.pk]['post'] = post
        displayed_posts[post.pk]['tags'] = post.tags.values_list('value', flat=True)

    return render(request, "app_site_main/blog.html", {"posts" : displayed_posts })

def blog_with_tag(request, tag_name, page_number=1):
    tag = Tag.objects.filter(value=tag_name)[0]
    posts = Post.objects.select_related().filter(tags = tag.pk)
    posts = posts.order_by('modified_at').reverse()[(page_number-1) *10 :page_number * 10]
    #get the posts tags
    displayed_posts = {}
    for post in posts:

        displayed_posts[post.pk] = {}
        displayed_posts[post.pk]['post'] = post
        displayed_posts[post.pk]['tags'] = post.tags.values_list('value', flat=True)
    return render(request, "app_site_main/blog.html", {"posts" : displayed_posts})

def about(request):
    return render(request, "app_site_main/about.html")



def other(request):
    return render(request, "app_site_main/other.html")
