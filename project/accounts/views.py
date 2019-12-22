from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"You account has beed created! You are able to log in")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'page_title': 'Sign Up'})
