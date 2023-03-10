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
from django.urls import path
import app_site_main.views, algorithms.views, nlp.views, radio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', app_site_main.views.about),
    path('', app_site_main.views.index),
    path('blog/<int:page_number>', app_site_main.views.blog),
    path('blog/<str:tag_name>/<int:page_number>', app_site_main.views.blog_with_tag),
    path('other/', app_site_main.views.other),
    path('algorithms/', algorithms.views.index),
    path('djikstras/', algorithms.views.djikstras),
    path('sorting-algos/', algorithms.views.sortingalgos),
    path('searching-algos/', algorithms.views.searchingalgos),
    path('nlp/', nlp.views.index),
    path('radio/', radio.views.index),
]
