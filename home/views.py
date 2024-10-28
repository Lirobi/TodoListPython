from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import TodoItem
from .forms import TodoItemForm
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "todos.html", {"todos": getTodos(request.user)})

def update(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST": #check if the request type is good
        if "id" in request.POST and "name" in request.POST:
            id = request.POST["id"]
            name = request.POST["name"]
            completed = False

            if len(name) >= 150:
                return redirect("todos")

            if "completed" in request.POST and request.POST["completed"] == "on":
                completed = True
            

            if "save" in request.POST:
                todoItem = TodoItem(id=id, name=name, completed=completed, user=request.user.username)
                todoItem.save()

            elif "delete" in request.POST:
                todoItem = TodoItem.objects.get(id=id)
                todoItem.delete()
        else:
            return render(request, "todos.html", {"error": "Unexpected error..."})
    else: 
        return render(request, "todos.html", {"error": "Invalid request"})
    
    return redirect("todos")





def login(request): # if logged in : go to account management
    if request.user.is_authenticated:
        return redirect("../todos")
    if request.method == "POST":
        if "login" in request.POST and "password" in request.POST: #if request not empty
            login_ = request.POST["login"]
            password = request.POST["password"]

            user = authenticate(username=login_, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect("../todos") #go to todos
                
            else:
                return render(request, "account.html", {"error" : "Error while authenticating, please retry later."}) # if unknow error
        
        
        else:
            missing = ""
            if "password" in request.POST:
                missing = "Please enter username."
            else:
                missing = "Please enter password."
            return render(request, "login.html", {"message": missing}) #if request is not good
    else:
      return render(request, "login.html")  

def register(request):
    if request.method == "POST":
        if "email" in request.POST and "username" in request.POST and "password" in request.POST:
            email = request.POST["email"]
            username = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.create_user(email=email, username=username, password=password)
            try:
                user.save()
            except Exception:
                return render(request, "register.html", {"error": str(Exception)})
            user = authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect("todos")
        else:
            missing = "Missing values"
            return render(request, "register.html", {"message": missing}) #if request is not good
    
    return render(request, "register.html")




def account(request):
    if request.user is not None:
        return render(request, "account.html")
    return redirect("login")


def logout_view(request):
    logout(request)
    return redirect('/')
    






#UTILS


def getTodos(user): #TODO Mettre user en paramètre et retourner ceux de cet utilisateur
    todos = []
    for item in TodoItem.objects.all().filter(user = user.username):
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