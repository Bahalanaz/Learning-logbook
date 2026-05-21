from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.http import JsonResponse

def home(request):
    name = request.GET.get('name','Guest')
    return HttpResponse(f"Hello {name}")

def about(request):
    return HttpResponse ("this is about")

def addstudent(request):
    Student.objects.create(name="Ali", age=20)
    return HttpResponse("student added")

def remove_all_student(request):
    Student.objects.all().delete()
    return HttpResponse("All students deleted")

def check(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    city = request.GET.get('city')
    country = request.GET.get('country')
    
    return JsonResponse({
        "name" : name,
        "age" : age,
        "city" : city,
        "country" : country
    })

def user(request,id):
    return HttpResponse(f"User ID is {id}")

def product(request,id):
    return HttpResponse(f"Product ID is: {id}")

def show_students(request):
    students = Student.objects.all()

    data = []

    for student in students:
        data.append({
            "id" : student.id,
            "name": student.name,
            "age": student.age
        })

    return JsonResponse({"students": data})

def count_students(request):
    students = Student.objects.all().count()
    return HttpResponse(f"number of students {students}")




