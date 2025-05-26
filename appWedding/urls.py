from django.urls import path
from . import views

app_name = 'appWedding'
urlpatterns = [
    path('', views.GoHome, name='home'),
    path('favorite/', views.GoFavorite, name='favorite'),
    path('ticket/', views.GoTicket, name='ticket'),
    path('ticket/entry/', views.GoTicketEntry, name='ticket_entry'),
    path('access/', views.GoAccess, name='access'),
    path('gallery/', views.GoGallery, name='gallery'),
    path('form/',views.FormView.as_view(), name='form'),
    path('profile/',views.GoProfile, name='profile'),
]