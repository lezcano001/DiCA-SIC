from django.urls import path

from . import views  # Esto básicamente importa views que se encuentra en esta misma página

urlpatterns = [
    path('', views.index, name="index")
]
