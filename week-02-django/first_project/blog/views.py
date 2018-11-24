# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
# Create your views here.
from .models import Article

def index(request):
    # random_number = randint(1, 10)
    # return HttpResponse("Hello, world." + random_number)
    # return HttpResponse("Hello, world. {}".format(random_number))
    # return HttpResponse("Hello, world. You're at the index.")
    # return render(request, "index.html", {})

    # name = "marco"
    # return render(request, "index.html", {"name" : name})
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title = "hello"
    #     contents = "this is a test"
    #     view_count = 0
    # )
    ctx = {
        "article_list" : article_list
    }
    return render(request, "index.html",ctx)
