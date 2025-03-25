from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import WarriorForm, CommentForm
from .models import Warrior, Comment


@login_required
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
def add_comment(request, warrior_id):
    warrior = get_object_or_404(Warrior, id=warrior_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.warrior = warrior
            comment.user = request.user
            comment.save()
            return render(request, 'warrior/warrior_detail.html', {'warrior': warrior})
        return render(request, 'warrior/warrior_detail.html', {'warrior': warrior})

@login_required
def warrior_detail(request, warrior_id):
    warrior = Warrior.objects.get(id=warrior_id)
    comments = Comment.objects.filter(warrior=warrior).order_by('-created_at')
    return render(request, 'warrior/warrior_detail.html', {'warrior': warrior, 'comments': comments,})