from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.conf import settings
User = settings.AUTH_USER_MODEL

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created! You are now able to log in ")
            return redirect("login")
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "users/register.html", context)
