from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.

def register(request):
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/registration.html', context)
    else:
        form = UserForm(request.POST)
        if form.is_valid:
            #creating user using form 
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            # return redirect('register-user')
            
            #create user using  create_user method 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            return redirect('register-user')
        


