from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from .forms import AnilistUserCreationForm, AnilistUserAuthenticationForm, AnilistUserChangeForm, ProfileChangeForm
from .models import AnilistUser, Profile


def index(request):
    return render(request, 'main/index.html')


class RegisterUserView(CreateView):
    form_class = AnilistUserCreationForm
    template_name = 'main/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return super().form_valid(user)

    def get_success_url(self):
        return reverse_lazy('personal_profile')


class AuthoriseUserView(LoginView):
    form_class = AnilistUserAuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('personal_profile')


class PersonalProfileView(LoginRequiredMixin, DetailView):
    template_name = 'main/my_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        profile = Profile.objects.get(pk=self.request.user.pk)
        return profile


class ProfileView(DetailView):
    pass


def logout_user(request):
    logout(request)
    return redirect('login')
