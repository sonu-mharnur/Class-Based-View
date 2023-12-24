from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Comments
from django.views import View
# Create your views here.

# def home(request):
#     return render(request,'index.html')


class MyTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagetitle"] = 'MyHomePage'
        context["name"] = 'Atul'
        return context
    
def AddCommentView(request):
    if request.method=='GET':
        comments = Comments.objects.all().order_by('-updatedat')
        context = {'comments': comments}
        return render(request, 'home.html', context)
    
    if request.method=='POST':
        comment = Comments.objects.create(comment=request.POST.get('comment'))
        comment.save()
        return redirect('add')
        
        
def ShowDetailView(request, pk):
    if request.method=='GET':
        comment = Comments.objects.get(id=pk)
        context = {'comment': comment}
        return render(request, 'update.html', context)
    
    if request.method=='POST':
        record = Comments.objects.get(id=pk)
        record.comment = request.POST.get('updated_comment')
        record.save()
        return redirect('add')


class DeleteView(View):
    def get(self, request, pk):
        comment = Comments.objects.get(id=pk)
        comment.delete()
        return redirect('add')
    