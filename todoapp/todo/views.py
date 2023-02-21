from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import RegisterForm, LoginForm
from .models import Tasks


# Create your views here.
#
# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse_lazy('task')




# class CustomRegisterView(RegisterView):
#     template_name = 'register.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse_lazy('tasks')
#


class Tasklist(ListView):
    model = Tasks  # table name
    context_object_name = 'task'  # url name
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')  # to redirect or back to other url
    template_name = 'TaskCreate.html'


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'TaskCreate.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskview.html'


def register_fun(request):
    context={}
    s = RegisterForm(request.POST )
    if s.is_valid():
        s.save()
        return redirect('/todo/task-list/')
    context['form'] = s
    return render(request,"register.html",context)



def login_fun(request):
    context={}
    s = LoginForm(request.POST )
    if s.is_valid():
        s.save()
        return redirect('/todo/task-list/')
    context['form'] = s
    return render(request,"login.html",context)





#
