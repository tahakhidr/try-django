from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(username=username, password=password)
        return redirect("/")
    return render(request, "accounts/login.html", context)
