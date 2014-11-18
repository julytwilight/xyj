# -*- coding: utf-8 -*-
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from ahead.utils.lazy import *
from ..forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "registration/login.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            user_cache = authenticate(username=form.cleaned_data.get('username'),
                                      password=form.cleaned_data.get('password1'))
            if user_cache:
                login(request, user_cache)
                return redirect('home')

        return render(request, "registration/login.html", {'form': form})


def logout(request):
    return logout_then_login(request, '/')


from django.contrib.auth.models Group
from ..models import User
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer