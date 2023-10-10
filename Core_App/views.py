from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    current_page = 'dashboard'
    context = {
        'current_page': current_page
    }
    return render (request, 'core/dashboard.html', context)