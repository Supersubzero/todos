
# Create your views here.
from django.shortcuts import render, redirect
from .models import TodoItem
from django.http import HttpResponse,JsonResponse

def home(request):
    todos = TodoItem.objects.all()
    return render(request, 'home.html', {'todos': todos})
    # return HttpResponse(todos)

def create(request):
    if request.method == 'POST':
        todo = TodoItem()
        todo.title = request.POST.get('title')
        todo.category = request.POST.get('category')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('/home/index')
    return render(request, 'create.html')

def update(request, id):
    todo = TodoItem.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.category = request.POST.get('category')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('/home/index')
    return render(request, 'update.html', {'todo': todo})

def delete(request, id):
    todo = TodoItem.objects.get(id=id)
    todo.delete()
    return redirect('/home/index')
