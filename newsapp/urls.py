from django.urls import path
from .views import Create, listfunc

urlpatterns = [
   path('', Create.as_view(), name='home'),
   path('/', listfunc, name='list'),
]
