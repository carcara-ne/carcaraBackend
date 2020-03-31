from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('relationship/scatter', views.scatter, name='scatter'),
    path('composition/pie', views.pie, name='pie'),
    path('distribution/scatter', views.scatter, name='scatter'),
    path('comparison/column', views.column, name='column'),
]
