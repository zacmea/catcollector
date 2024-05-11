from django.shortcuts import render

cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Tom', 'breed': 'Tom', 'description': 'gentle and loving', 'age': 0},
]
# Create your views here.
def home(request):
    return render(request, 'home.html',) # this is the home route, the same as '/'. the name arg is a keyword arg that we can use to refer to this path in other parts of our code

def about(request):
    return render(request, 'about.html',) # this is the about route, the same as '/about/'

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats}) # this is the cats route, the same as '/cats/'