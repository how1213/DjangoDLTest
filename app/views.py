from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import FileForm, UserChangeForm

from .models import File

@login_required
def index(request):
    files = File.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'files':files})
    
@login_required
def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    files = user.file_set.all().order_by('-created_at')
    return render(request, 'app/users_detail.html', {'user': user, 'files':files})

@login_required
def users_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserChangeForm(request.POST or None, instance=user)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("app:index")
    context = {
        "form": form,
    }
    return render(request,'app/users_edit.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def files_new(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
        return redirect('app:users_detail', pk=request.user.pk)
    else:   
        form = FileForm()
    return render(request, 'app/files_new.html', {'form': form})

@login_required
def files_detail(request, pk):
    files = get_object_or_404(File, pk=pk)
    return render(request, 'app/files_detail.html', {'files':files})