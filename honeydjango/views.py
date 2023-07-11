from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
def testimonial(request):
    return render(request, "testimonial.html")
def contact(request):
    return render(request, "contact.html")
def chocolate(request):
    return render(request, "chocolate.html")


