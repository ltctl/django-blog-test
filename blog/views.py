import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from blog.models import Article, Category, Comment


# Homepage
def index(request):
    article_list = Article.objects.all().order_by('-date_time')[0:5]
    return render(request, 'blog/index.html', {"article_list": article_list,
                                               "source_id": "index"})


# List View for the Blog
def articles(request, pk):
    pk = int(pk)
    if pk:
        category_object = get_object_or_404(Category, pk=pk)
        category = category_object.name
        article_list = Article.objects.filter(category_id=pk)
    else:
        # pk为0时表示全部
        article_list = Article.objects.all()  # 获取全部文章
        category = u''
    return render(request, 'blog/articles.html', {"article_list": article_list,
                                                  "category": category,
                                                  })


def about(request):
    return render(request, 'blog/about.html')


def archive(request):
    article_list = Article.objects.order_by('-date_time')
    return render(request, 'blog/archive.html', {"article_list": article_list})


def link(request):
    return render(request, 'blog/link.html')


def message(request):
    return render(request, 'blog/message_board.html', {"source_id": "message"})


# Receive comment and POST back
@csrf_exempt
def getcomment(request):
    arg = request.POST
    data = arg.get('data')
    data = json.loads(data)
    title = data.get('title')
    url = data.get('url')
    source_id = data.get('sourceid')
    if source_id not in ['message']:
        article = Article.objects.get(pk=source_id)
        article.commenced()
    comments = data.get('comments')[0]
    content = comments.get('content')
    user = comments.get('user').get('nickname')
    Comment(title=title, source_id=source_id, user_name=user, url=url, comment=content).save()
    return JsonResponse({"status": "ok"})


# Details of the Blog
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.viewed()
    return render(request, 'blog/detail.html', {"article": article,
                                                "source_id": article.id})


def search(request):
    key = request.GET['key']
    article_list = Article.objects.filter(title__icontains=key)
    return render(request, 'blog/search.html',
                  {"article_list": article_list, "key": key})


def tag(request, name):
    article_list = Article.objects.filter(tag__tag_name=name)
    return render(request, 'blog/tag.html', {"article_list": article_list,
                                             "tag": name})
