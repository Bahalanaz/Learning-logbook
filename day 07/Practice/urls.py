from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('add_student/', views.addstudent),
    path('remove_all_student/', views.remove_all_student),
    path('check/', views.check),
    path('user/<int:id>/', views.user),
    path('product/<int:id>/', views.product),
    path('show_students/', views.show_students),
    path('count_students/', views.count_students)

]
