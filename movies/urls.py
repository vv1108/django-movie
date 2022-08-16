from . import views
from django.urls import path


app_name = "movies"
urlpatterns = [
    path('', views.index_view, name='index'),
]
