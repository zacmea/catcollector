from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',) # this is the home route, the same as '/'. the name arg is a keyword arg that we can use to refer to this path in other parts of our code

def about(request):
    return render(request, 'about.html',) # this is the about route, the same as '/about/'