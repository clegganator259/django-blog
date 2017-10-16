from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import Http404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts' : posts,'page_title':'Main Page'})

def article(request,post_title):
    print("article")
    print(post_title)
    escaped_post_title = ' '.join(post_title.split('_'))
    print(escaped_post_title)
    post = Post.objects.all().filter(title__iexact=escaped_post_title)
    if not post:
        raise Http404("Page does not exist")
    return render(request, 'blog/article.html',{'post':post[0],'page_title':post[0].title})
# Create your views here.
