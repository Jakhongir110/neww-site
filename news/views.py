from django.shortcuts import render, redirect
from django.views import View
from .models import Article, Category
# Create your views here.

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        articles = Article.objects.all()
        main_news = articles[:7]
        featured_news = articles.order_by("?")[:10]
        latest_news = articles.order_by("-id")[:8]
        
        context = {
            "categories": categories,
            "main_news": main_news,
            "featured_news": featured_news,
            "latest_news": latest_news,
        }
        return render(request, 'index.html', context)
