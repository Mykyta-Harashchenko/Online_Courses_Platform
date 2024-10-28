from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages


from .forms import RegisterForm

def main(request):
    return render(request, 'app_auth/index.html')

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
            return redirect(to='app_auth/registration:signin')
        return render(request, self.template_name, {'form': form})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='app_auth:root')
