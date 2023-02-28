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

    #when filtering for tags, I Can't just pass a string.  I have to pass the tag id, which for main is 3.
    #another way to do this is to just filter the tags and get the string from the numbers, but this works too.  I'll just
    # log the tag ids for now.
    posts = Post.objects.filter(tags__in=[3])
    posts = posts.order_by('modified_at').reverse()[(page_number-1) *10 :page_number * 10]
    logger.debug("Got %d posts", len(posts))
    return render(request, "app_site_main/index.html", {"posts": posts})

def about(request):
    return render(request, "app_site_main/about.html")

'''
what I would like to do here is to 
have multiple pages
'''
def blog(request, page_number=1):
    posts = Post.objects.exclude(tags__in=[3])
    posts = posts.order_by('modified_at').reverse()[(page_number-1) *10 :page_number * 10]
    return render(request, "app_site_main/blog.html", {"posts" : posts})

def other(request):
    return render(request, "app_site_main/other.html")