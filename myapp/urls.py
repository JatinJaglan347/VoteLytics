from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('create-voting/', views.vote ,name='create-voting'),
    path('vote/home/', views.home, name='home'),
    path('vote/success/', views.vote_success, name='vote_success'),
    path('vote/', views.combined_view, name='vote'),
    path('select_voting/', views.voting, name='select_voting'),
    path('services/', views.services, name='services'),
    path('create/', views.create, name='create'),
    path('results/',views.graph_view,name='results'),
    path('to_create/',views.to_create,name='to_create'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about')
]