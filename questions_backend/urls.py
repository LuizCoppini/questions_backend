from django.contrib import admin
from django.urls import path
from quiz.views import questions_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/questions/', questions_list, name='questions_list'),
]
