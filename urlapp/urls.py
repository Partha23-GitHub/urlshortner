from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='basepage'),
    path('urlshort/',views.urlShotrener,name='urlshortner'),
]