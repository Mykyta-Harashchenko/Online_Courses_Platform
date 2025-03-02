from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import WarriorForm
from .models import Warrior


@login_required  # Требуем аутентификацию
def add_warrior(request):
    if request.method == 'POST':
        form = WarriorForm(request.POST, request.FILES)  # Добавили request.FILES
        if form.is_valid():
            warrior = form.save(commit=False)
            warrior.user = request.user
            warrior.save()
            return redirect('app_auth:root_paginate', page=1)
        else:
            print(form.errors)
    else:
        form = WarriorForm()
    return render(request, 'warrior/templates/add_warrior.html', {'form': form})

@login_required
def warrior_detail(request, warrior_id):
    warrior = Warrior.objects.get(id=warrior_id)
    return render(request, 'warrior/warrior_detail.html', {'warrior': warrior})