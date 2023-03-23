"""site_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import app_site_main.views, algorithms.views, nlp.views, radio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', app_site_main.views.about),
    path('', app_site_main.views.index),
    path('blog/<int:page_number>', app_site_main.views.blog),
    path('new_post/', app_site_main.views.new_post),
    path('blog/<str:tag_name>/<int:page_number>', app_site_main.views.blog_with_tag),
    path('sfo_lord_differences/', app_site_main.views.sfo_lord_differences),
    path('getlordimage/<str:lord_name>', app_site_main.views.getlordimage),
    path('algorithms/', algorithms.views.index),
    path('djikstras/', algorithms.views.djikstras),
    path('sorting-algos/', algorithms.views.sortingalgos),
    path('linear-search/', algorithms.views.linearsearch),
    path('binary-search/', algorithms.views.binarysearch),
    path('nlp/', nlp.views.index),
    path('radio/', radio.views.index),
    path('little_lemon/', include('little_lemon.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

