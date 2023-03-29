from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import Tasklist, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView, HomePageView

urlpatterns = [
    path('task/', Tasklist.as_view(), name='task'),  # asview=  class based
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-view/<int:pk>/', TaskDetailView.as_view(), name='task-view'),
    path('home/', HomePageView.as_view(), name='home'),
    path('login/',views.login_1,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.signout, name='logout')



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)