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


def index(request):
    #Post object only queried every 300 seconds, all other responses come
    #from cache.  Dont cache stuff whose content relies on logged in user.
    #from django.http import HttpResponse
    #return HttpResponse(str(request.user).encode("ascii"))
    #only load posts that have a publication date in the past
    posts = Post.objects.all()
    logger.debug("Got %d posts", len(posts))
    return render(request, "app_site_main/index.html", {"posts": posts})