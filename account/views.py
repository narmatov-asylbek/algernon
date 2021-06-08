from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http.response import JsonResponse
from django.contrib import messages

from .forms import LoginForm, SettingsForm, ContactForm, CustomUserCreationForm
from books.models import Book, Library
from .models import Contact, CustomUser


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'account/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли в аккаунт')
                    return redirect('/')
                messages.error(request, 'Аккаунт заблокирован')
                return redirect('/')
            messages.error(request, 'Неправильные данные. Проверьте правильность')
            return render(request, 'account/login.html', {'form': form})


class UserSettingsUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        settings_form = SettingsForm(instance=request.user)
        contact_form = ContactForm(instance=request.user.contact)
        context = {
            'settings_form': settings_form,
            'contact_form': contact_form,
        }
        return render(request, 'account/settings_form.html', context)


@require_POST
def update_user_settings(request):
    settings_form = SettingsForm(request.POST, request.FILES, instance=request.user)

    if settings_form.is_valid():
        settings_form.save()
        return redirect('account:settings')
    messages.error(request, "Произошла ошибка")
    return redirect('account:settings')


@require_POST
def update_user_contacts(request):
    contact_form = ContactForm(request.POST, request.FILES, instance=request.user.contact)

    if contact_form.is_valid():
        contact_form.save()
    return redirect('account:settings')


class UserRegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'account/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Contact.objects.create(user=user)
            Library.objects.get_or_create(user=user)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли в аккаунт')
                    return redirect('/')
                messages.error(request, 'Аккаунт заблокирован')
                return redirect('/')
        messages.error(request, 'Произошла ошибка')
        return render(request, 'account/registration.html', {'form': CustomUserCreationForm()})


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')
        return redirect('/')


class ProfileInfoView(LoginRequiredMixin, View):
    def get(self, request, slug):
        user = CustomUser.objects.get(slug=slug)
        context = {
            'user': user,
            'profile_active': True
        }
        return render(request, 'account/profile.html', context)


class AccountLibraryView(View):
    def get(self, request, slug):
        user = CustomUser.objects.get(slug=slug)
        library = Library.objects.get(user=user)

        context = {
            'library': library,
            'user': user,
            'lib_active': True
        }
        return render(request, 'books/book_library.html', context)