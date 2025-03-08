from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use AuthenticationForm
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully.")
                return redirect('chat_room', room_name=user.username)  # Redirect to chat page after successful login
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()  # Instantiate an empty form

    return render(request, 'login.html', {'form': form})

def chat(request):
    # This view renders the chat page for logged-in users
    if request.user.is_authenticated:
        return render(request, 'chat.html')  # Render your chat page
    else:
        return redirect('login')


# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect the user to the login page after logout
