from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from articles.models import Article
from comments.forms import CommentForm
from comments.models import Comment


# Create your views here.
class ArticleView(View):
    
    def get(self, request, *args, **kwargs):
        article = Article.objects.first()
        form = CommentForm()
        comments = Comment.objects.all()
        context = {'article': article, 'form': form, 'comments': comments}
        
        return render(request, "index.html", context=context)

    def post(self, request, *args, **kwargs):
        article = Article.objects.first()
        form = CommentForm(request.POST)
        
        # Random get a user
        user = User.objects.first()
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.content_object = article
            comment.save()
        return redirect('index')
