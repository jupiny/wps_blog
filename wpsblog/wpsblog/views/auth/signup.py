from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import View


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "auth/signup.html",
            {},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect(
            "auth:login"
        )
