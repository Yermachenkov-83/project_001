from django.shortcuts import render

from django.views.generic.base import View

from .models import *


# class MainView(View):
#     def get(self, request):
#         activity = Activity.objects.all()
#         return render(request, "app_01/activity_list.html", {"activity_list": activity})


def test_view(request):
    return render(request, 'base.html')
