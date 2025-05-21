from django.urls import path
from .views import *

app_name = 'app' #= app:index
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('movie/<int:id>/', SingleView.as_view(), name='singlePage'),
    path('article/<int:id>/', ArticleView.as_view(), name='articlePage'),
]