from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def page_view(request, page=1):
    article_list = Article.objects.filter(published=True)
    my_site = Site.objects.all()[0]
    paginator = Paginator(article_list, my_site.article_num)

    featured_tags = Tag.objects.order_by('size')[:3]
    featured_categories = Category.objects.order_by('size')[:3]

    try:
        artiles = paginator.page(page)
    except PageNotAnInteger:
        artiles = paginator.page(1)
    except EmptyPage:
        artiles = paginator.page(paginator.num_pages)

    return render(request, 'myBlog/pages.html',{
        'articles':artiles,
        'site':my_site,
        'featured_tags':featured_tags,
        'featured_categories':featured_categories
    })


def article_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    my_site = Site.objects.all()[0]
    return render(request, 'myBlog/article.html', {'article': article, 'site': my_site})


def categories_view(request):

    return render(request, 'myBlog/categories.html', {'categories': Category.objects.all(), 'site': Site.objects.all()[0]})


def tags_view(request):

    return render(request, 'myBlog/tags.html', {'tags': Tag.objects.all(), 'site': Site.objects.all()[0]})


