from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Article
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

class HomeView(View):
    def get(self, request):
        # categories = Category.objects.all()
        articles = Article.objects.all()
        main_news = articles[:7]
        featured_news = articles.order_by("?")[:10]
        latest_news = articles.order_by("-id")[:8]
        
        context = {
            # "categories": categories,
            "main_news": main_news,
            "featured_news": featured_news,
            "latest_news": latest_news,
        }
        return render(request, 'index.html', context)

class ArticleDetailView(View):
    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        article.views += 1
        article.save()
        
        similar_news = Article.objects.filter(category = article.category).exclude(id=id).order_by("?")[:4]
        context = {
            'article': article,
            'similar_news': similar_news,
        }
        return render(request, "single.html", context)
    
class ContactView(View):
    form_class = ContactForm
    def get(self,request):
        return render(request, 'contact.html')
    
    def post(self,request):
        data = request.POST
        form = self.form_class(data=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message sent")
            return redirect("contact")
        messages.error(request,"Something went error")
        return render(request, "contact.html")