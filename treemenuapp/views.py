from django.shortcuts import render
from .models import Rubric


def menu(request):
    return render(request, 'treemenuapp/menu.html', {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass
