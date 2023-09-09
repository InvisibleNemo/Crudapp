from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView, UpdateView
from .forms import SignupForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import ProfileForm

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
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'
    def get_success_url(self):
        # Define the URL to redirect to after a successful login
        return reverse_lazy('dashboard')  # Replace 'dashboard' with the name of your dashboard URL pattern
    
class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'home/user_profile.html'
    model = CustomUser  # Use the User model

    def get_object(self, queryset=None):
        # Retrieve the user's profile based on the 'pk' parameter in the URL
        pk = self.kwargs.get('pk')
        return self.model.objects.get(pk=pk)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'home/user_profile.html'  # You can reuse the same template for both viewing and editing
    # success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Return the currently logged-in user's profile for editing
        return self.request.user

    def form_valid(self, form):
        # Save the form and update the user's profile
        form.save()
        # Redirect to the 'profile' view with the 'pk' parameter
        return redirect('profile', pk=self.request.user.pk)