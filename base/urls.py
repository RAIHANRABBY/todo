from django.urls import path
from . import views
urlpatterns = [   
    path('',views.homeView,name='home'),
    path('delete/<str:pk>',views.remove_event,name='delete')
]
