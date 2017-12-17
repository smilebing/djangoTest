from django.contrib import admin
from .models import BlogDetail
from .models import Article
# Register your models here.

admin.site.register(BlogDetail)
admin.site.register(Article)