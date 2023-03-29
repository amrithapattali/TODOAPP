from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

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


class HomePageView(TemplateView):
    template_name = 'home.html'

class Tasklist(ListView):
    model = Tasks  # table name
    context_object_name = 'task'  # url name
    template_name = 'tasklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count'] = context['task'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task'] = context['task'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context


class TaskCreate(CreateView):
    model = Tasks
    fields = ['title', 'completed']
    success_url = reverse_lazy('task')  # to redirect or back to other url
    template_name = 'TaskCreate.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


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


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        return redirect('login')

    return render(request, 'register.html')


def login_1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, 'tasklist.html', {'fname': fname})

        else:
            return redirect('login')

    return render(request, 'login.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully!')
    return redirect('login')


