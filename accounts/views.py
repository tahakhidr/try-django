from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "accounts/register.html", context)
