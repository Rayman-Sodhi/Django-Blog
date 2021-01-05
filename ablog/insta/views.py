from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail',args=[str(pk)]))

class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    ordering=['-id']


class ArticleDetailView(DetailView):
    model= Post
    template_name = 'detail.html'

def get_context_data(self,*args, **kwargs):
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"]=total_likes

class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields= '__all__'

class UpdatePostView(UpdateView):
        model = Post
        form_class = EditForm
        template_name = 'update.html'
       # fields= ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
