from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return HttpResponse("Pizza store")

def register(request):
    form=UserCreationForm;
    return render(request, 'orders/signup.html', {form})
