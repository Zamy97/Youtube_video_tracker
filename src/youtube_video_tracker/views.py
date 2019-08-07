from django.shortcuts import render
# from django.template.loader import get_complete

def home_page(request):
    context = { "title": "Welcome to Youtube Video Tracker"}
    return render(request, "home_view.html", context)

def login_form(request):
    return render(request, "login_form.html", {"title": "Log In"})

def add_song_form(request):
    return render(request, "add_song_form.html", {"title": "Add Song"})

def signup_form(request):
    return render(request, "signup_form.html", {"title": "Sign Up"})
