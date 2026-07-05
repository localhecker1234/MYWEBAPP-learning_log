from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    '''Register a new user'''
    if request.method != 'POST':
        #Display blank registration form
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            form.save()
            #Log in the user and then redirect to home page.
            login(request, new_user) ## Takes two thing request and new user object
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)    



def custom_logout(request):
    logout(request)
    return redirect('learning_logs:index')  # Change to your intended landing page
