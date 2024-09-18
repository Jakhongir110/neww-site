from django.db import models
from accounts.models import User
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
       
    def __str__(self):
        return self.name
    
class Tag(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Article(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to="articles")
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField(Tag, related_name='articles', null=True)
    
    def __str__(self):
        return f"{self.id} {self.title}"