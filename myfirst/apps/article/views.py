from django.shortcuts import render
from .models import Article
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    lst_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'article/list.html', {'lst_article_list': lst_article_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)

    except:
        raise Http404('Статья не найдена')
    lst_comm = a.comment_set.order_by('-id')
    return render(request, 'article/detail.html', {'article': a, 'comm_lst': lst_comm})


def comm(request, article_id):
    try:
        a = Article.objects.get(id=article_id)

    except:
        raise Http404('Статья не найдена')
    a.comment_set.create(autor_name=request.POST['name'], comm_text=request.POST['text'])
    return HttpResponseRedirect(reverse('article:detail', args=(a.id,)))


def glav(request):
    return render(request, 'article/index.html')


def add_author(request):
    pass
