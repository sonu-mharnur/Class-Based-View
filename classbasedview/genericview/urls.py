from django.urls import path
from . import views
# from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('', views.MyTemplateView.as_view(), name='home'),
    path('create/', views.CreateUser.as_view(), name='create'),


]