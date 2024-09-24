from .models import Category

def get_main_context(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return context