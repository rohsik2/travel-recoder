from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path('', views.travel_view, name='travel'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('<int:id>/<int:date>', views.detail_day_view, name='detail_day'),
    path('test/',views.test_view, name='test')
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)