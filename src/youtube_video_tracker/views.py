from django.shortcuts import render
# from django.template.loader import get_complete

def home_page(request):
    context = { "title": "Welcome to Youtube Video Tracker"}
    return render(request, "home_view.html", context)
