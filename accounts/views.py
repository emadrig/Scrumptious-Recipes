from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from accounts.forms import SignUpForm, LoginForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            if password == password_confirmation:
                # create a new user with those values
                user = User.objects.create_user(
                    username,
                    password = password,
                    first_name = first_name,
                    last_name = last_name,
                )

                # login the user
                login(request, user)
                return redirect("recipe_list")

            else:
                form.add_error("password", "Passwords do not match")

    else:
        form = SignUpForm()

    context = {
        "form":form,
    }

    return render(request, "accounts/signup.html", context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(
                request,
                username=username,
                password= password
                )

            if user is not None:
                login(request, user)
                # redirect to a success page
                return redirect("recipe_list")

    else:
        # return to an invalid login error message
        form = LoginForm()
    context ={
        "form":form,
    }
    return render(request, "accounts/login.html",context)


def user_logout(request):
    logout(request)
    return redirect("recipe_list")

