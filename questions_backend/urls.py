from django.contrib import admin
from django.urls import path
from quiz.views import questions_list, search_random_question, procedural_question

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/questions/', questions_list, name='questions_list'),
    path('api/search_random_question/', search_random_question, name='search_random_question'),
    path('api/procedural_question/', procedural_question, name='procedural_question'),
]
