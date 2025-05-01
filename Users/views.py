from django.contrib import messages
from django.shortcuts import render, redirect

from django.views import View

from .forms import RegisterForm

# Create your views here.
class Register(View):
    def get(self, request):
        register_form_data = request.session.get('register_form_data', None)
        form = RegisterForm(register_form_data)
        return render(request, 'Users/pages/register.html', {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        request.session['register_form_data'] = request.POST
        
        if form.is_valid():
            form.save(commit=False)
            messages.success(request, 'Your user is created, please log in.')
            del(request.session['register_form_data'])
            return redirect('Users:Login')
        
        
        return redirect('Users:Register')
    
class Login(View):
    def get(self, request):
        return render(request, 'Users/pages/login.html')