from django.urls import path
from . import views

app_name = 'appName1'
urlpatterns = [
    path('<int:course_id>/', views.details, name='details-page'),
    path('', views.courses, name='home-page'),
    path('<int:course_id>/your_choice', views.your_choice, name='your_choice'),
]
