from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import todolistitem
from django.http import HttpResponseRedirect

def todoappview(request):
    all_todo_items = todolistitem.objects.all()
    return render(request,'todolist.html',{'all_items':all_todo_items})

# Create your views here.
def addtodoview(request):
    x= request.POST['content']
    if x == '':
      print("Enter an task")
    else:
       new_item = todolistitem(content = x)
       new_item.save()
    return HttpResponseRedirect('/todoapp/')
def deletetodoview(request, i):
    y = todolistitem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')