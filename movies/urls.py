from . import views
from django.urls import path


app_name = "movies"
urlpatterns = [
    path('index/', views.index_view, name='index'),
]
