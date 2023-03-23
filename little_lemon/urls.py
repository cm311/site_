from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/', views.book, name="book"),
    path('home_form/', views.form_view, name="form_view"),
    path('booking_form/', views.booking_form_view, name='booking_form_view')
]