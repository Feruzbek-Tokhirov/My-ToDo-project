from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import TodoForms
from .models import Todo


@login_required
def index(request):
    user = request.user
    todos = Todo.objects.filter(author=user).order_by('-id')
    status = request.GET.get('status')
    q = request.GET.get('q')
    priority = request.GET.get('priorty')
    if priority:
        todos = todos.filter(priority=priority)
    if q:
        todos = todos.filter(title__icontains=q)
    if status:
        todos = todos.filter(status__exact=status)
    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)


@login_required
def created(request):
    form = TodoForms(request.POST or None)
    if form.is_valid():
        auth = form.save(commit=False)
        auth.author = request.user
        auth.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'crud/created.html', ctx)


@login_required
def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForms(request.POST or None, instance=todo)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('/')
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, 'crud/single.html', context)


@login_required
def delete(request, pk):
    obj = request.GET.get('ans')
    todo = Todo.objects.get(id=pk)
    if obj:
        Todo.objects.get(id=pk).delete()
        return redirect('/')
    ctx = {
        'todo': todo
    }
    return render(request, 'crud/delete.html', ctx)


def login_view(request):
    if not request.user.is_anonymous:
        return redirect(index)
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            # messages.success(request, "Muvaffaqiyatli royhatdan otdingiz")
            if next_path:
                return redirect(next_path)
            return redirect(index)
    ctx = {
        'form': form
    }
    return render(request, 'registration/login.html', ctx)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        # messages.success(request, "Muvaffaqiyatli royxatdan chiqdingiz")
        logout(request)
        return redirect('login')
    return render(request, 'registration/logged_out.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.success(request, "Muvaffaqiyatli royhatdan otdingiz")
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context)
