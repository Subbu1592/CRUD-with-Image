from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'galary', views.GalaryViewSet)
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('crudlist/', views.crudlist, name='crudlist'),
    path('edit/<int:iid>', views.edit, name='edit'),
    path('delete/<int:iid>', views.delete, name='delete'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]


router = routers.DefaultRouter()
router.register(r'galary', views.GalaryViewSet)