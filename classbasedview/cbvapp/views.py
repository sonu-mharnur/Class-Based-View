from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Comments
from django.views.generic import ListView

from django.views import View


class ShowListView(ListView):
    model = Comments
    template_name = 'showcomments.html'
    context_object_name = 'allcomments'
    # queryset = Comments.objects.filter()

print(dir(ShowListView()))


# print(dir(View))
# Create your views here.
# def home(request):
#     return render(request, 'index.html')

#print(dir(TemplateView))

class MyTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagetitle"] = 'MyHomePage'
        context["name"] = 'Sakeeb'

        return context
  

class AddCommentView(View):
    def get(self, request):
        comments = Comments.objects.all().order_by('-updatedat')
        context = {'comments': comments}
        return render(request, 'home.html', context)
    
    def post(self, request):
        comment = Comments.objects.create(comment=request.POST.get('comment'))
        comment.save()
        return redirect('add')
    
class ShowDetailView(View):
    def get(self, request, pk):
        comment = Comments.objects.get(id=pk)
        context = {'comment': comment}
        return render(request, 'update.html', context)
    
    def post(self, request, pk):
        record = Comments.objects.get(id=pk)
        record.comment = request.POST.get('updated_comment')
        record.save()
        return redirect('add')
    

class DeleteView(View):
    def get(self, request, pk):
        comment = Comments.objects.get(id=pk)
        comment.delete()
        return redirect('add')