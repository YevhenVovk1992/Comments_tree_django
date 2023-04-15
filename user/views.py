import os

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.urls import reverse
from django.views import View

from user.forms import SignUpForm, LoginForm, ProfileUpdateForm


class StartPageView(View):

    def get(self, request):
        """
        Get start page for user
        """
        return render(request, "user/start_page.html")


class SignUpView(View):

    def get(self, request):
        """
        Registration new user. Render HTML page with the form
        """
        form = SignUpForm()
        return render(request, "user/signup.html", {"form": form})

    def post(self, request):
        """
        Registration new user. Get data from the form and create new user
        """
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("user:user_profile"))
        form.add_error(None, "Form is not valid")
        return render(request, "user/signup.html", {"form": form})


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("user:user_profile"))
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect(reverse("user:user_profile"))
            form.add_error(None, "Invalid username or password")
        return render(request, "user/login.html", {"form": form})


class UserProfileView(View):

    def get(self, request):
        profile_form = ProfileUpdateForm()
        context = {
            'p_form': profile_form
        }
        return render(request, 'user/profile.html', context)

    def post(self, request):
        user = request.user
        old_avatar = user.profile.avatar
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            if old_avatar:
                os.remove(old_avatar.path)
        return redirect(reverse("user:user_profile"))
