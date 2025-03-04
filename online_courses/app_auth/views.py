from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages


from .forms import RegisterForm, ProfileForm
from .models import Profile
from warrior.models import Warrior


def main(request, page=1):
    warriors = Warrior.objects.all().order_by('first_name')
    paginator = Paginator(warriors, 10)
    warriors_page = paginator.get_page(page)
    return render(request, 'app_auth/index.html', {'warriors': warriors_page})



class RegisterView(View):
    template_name = 'app_auth/registration/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(f'Form is received')
        if form.is_valid():
            print(f'Form is valid')
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Вітаємо, {username}. Ваш аккаунт успішно створено')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})

@login_required
def profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='app_auth:profile')

    warriors = Warrior.objects.filter(user=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'app_auth/registration/profile.html', {'profile_form': profile_form, 'warriors': warriors})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='app_auth:root')



# Uganda228
