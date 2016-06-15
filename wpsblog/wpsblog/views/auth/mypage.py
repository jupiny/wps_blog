from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "auth/mypage.html"
