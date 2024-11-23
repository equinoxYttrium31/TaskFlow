from django.shortcuts import render

# Create your views here.
def home_view(request):
    template = "MainPage.html"
    context = {
        'message': 'Welcome to TaskFlow',
    }
    return render(request, template, context)

def Login(request):
    template = "Login.html"
    return render(request, template)