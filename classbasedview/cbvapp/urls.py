from django.urls import path
from . import views
# from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', views.MyTemplateView.as_view(), name='home'),
    path('add/', views.AddCommentView.as_view(), name='add'),
    path('details/<int:pk>', views.ShowDetailView.as_view(), name='details'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
    path('showdetails/', views.ShowListView.as_view(), name='showlist'),
]