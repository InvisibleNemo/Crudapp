from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import SignupForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'home/registration/login.html'  # Create this template
    success_url = reverse_lazy('dashboard')  # Replace 'dashboard' with the actual name of your DashboardView
    # def get_success_url(self):
    #     # Define the URL to redirect to after a successful login
    #     return redirect('dashboard')  # Replace 'dashboard' with the name of your dashboard URL pattern
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('logout') 

class SignUpView(CreateView):
    template_name = 'home/registration/signup.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL after registration

        # Handle form errors if registration fails
        return render(request, self.template_name, {'form': form})
    
class DashboardView(TemplateView):
    template_name = 'home/dashboard.html'
    def get_success_url(self):
        # Define the URL to redirect to after a successful login
        return reverse_lazy('dashboard')  # Replace 'dashboard' with the name of your dashboard URL pattern