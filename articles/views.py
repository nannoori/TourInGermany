from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CommentForm

def article_list(request):
    articles = Article.objects.all().order_by('-date');
    query=request.GET.get("q")
    if query:
        articles=articles.filter(title__icontains=query)
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })
def add_comment(request, slug):
    articles = get_object_or_404(Article, slug = slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.articles = articles
            comment.save()
            return redirect('articles:article_detail', slug = articles.slug)
        else:
            return HttpResponse("Fixed. --AF")
    else:
        form = CommentForm()
        template = 'articles/templates/add_comment.html'
        context = {'form': form}
        return render (request.template.context)
