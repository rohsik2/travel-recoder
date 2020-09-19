from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('', views.travel_view, name='travel_view'),
    path('<int:id>/', views.detail_view, name='detail_view'),
    path('<int:id>/new', views.new_location_view, name='new_location_view'),
    path('test/',views.test_view, name='test_view'),
    path('new/',views.post_new, name='new_view')
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)