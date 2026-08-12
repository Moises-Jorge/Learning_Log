from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
			'form': form,
		}
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)
            return redirect('index')
        context = {
			'form': form,
		}
        return render(request, 'users/register.html', context)
