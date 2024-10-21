from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import TodoItem
from .forms import TodoItemForm
from django.contrib.auth import authenticate


# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    return render(request, "todos.html", {"todos": getTodos()})

def update(request):
    if request.method == "POST":
        if "id" in request.POST and "name" in request.POST:
            id = request.POST["id"]
            name = request.POST["name"]
            completed = False

            if len(name) >= 150:
                return HttpResponseRedirect("../todos")

            if "completed" in request.POST and request.POST["completed"] == "on":
                completed = True
            

            if "save" in request.POST:
                todoItem = TodoItem(id=id, name=name, completed=completed)
                todoItem.save()

            elif "delete" in request.POST:
                todoItem = TodoItem.objects.get(id=id)
                todoItem.delete()


    return HttpResponseRedirect("../todos")

def account(request):
    if request.method == "POST":
        if "login" in request.POST and "password" in request.POST:
            login = request.POST["login"]
            password = request.POST["password"]

            user = authenticate(username=login, password=password)
            if user is not None:
                pass
            else:
                return render(request, "account.html", {"error" : "Error while authenticating, please retry later."})
        else:
            return render(request, "account.html", {"error" : "Invalid credentials"})
    return HttpResponseRedirect("../todos")

#TODO : faire la connection user, associer un userid à un todo. ne charger que les todos qui ont l'user id de l'utilisateur connecté










#UTILS


def getTodos(): #TODO Mettre user en paramètre et retourner ceux de cet utilisateur
    todos = []
    for item in TodoItem.objects.all():
        form = TodoItemForm(instance=item)
        todos.append(form)

    

    idList = TodoItem.objects.values_list('id', flat=True)
    newId = -1
    i = 0
    while newId < 0:
        if i not in idList:
            newId = i
        i+=1
        

    newItem = TodoItem(id=newId)

    todos.append(TodoItemForm(instance=newItem))
    return todos