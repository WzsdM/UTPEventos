from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def adEventos(request):
    return render(request, 'admin_eventos.html')
def Login(request):
    return render(request, 'login.html')