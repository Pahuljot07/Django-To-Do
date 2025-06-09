from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegisterForm
from .models import Task
from .forms import TaskForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'todo/home.html'

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'todo/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'todo/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'todo/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task-list')
        return render(request, 'todo/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@method_decorator(login_required, name='dispatch')
class TaskListView(View):
    def get(self, request):
        return render(request, 'todo/task_list.html')
    
@method_decorator(login_required, name='dispatch')
class TaskListView(View):
    def get(self, request):
        query = request.GET.get('q')
        tasks = Task.objects.filter(user=request.user)

        if query:
            tasks = tasks.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
)


        pending_tasks = tasks.filter(is_completed=False)
        completed_tasks = tasks.filter(is_completed=True)

        return render(request, 'todo/task_list.html', {
            'pending_tasks': pending_tasks,
            'completed_tasks': completed_tasks,
            'query': query
        })


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
