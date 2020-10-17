from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse,reverse_lazy
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from app_blog.models import Blog,Comment,Likes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import uuid
from .forms import CommentForm
# Create your views here.


class CreateBlog(LoginRequiredMixin,CreateView):
    template_name = 'app_blog/create_blog.html'
    model = Blog
    fields = ('blog_title','blog_content','blog_image')
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-')+'-'+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog_list.html'


@login_required
def blogDetails(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('app_blog:blog_details' , kwargs={'slug':slug}))
    return render(request,'app_blog/blog_details.html',context={'blog':blog, 'comment_form':comment_form })