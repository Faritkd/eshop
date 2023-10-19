from django.shortcuts import render
from django.views.generic.list import ListView
from article_module.models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/article_page.html'

