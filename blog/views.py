from django.http import HttpResponse
from .models import BlogDetail
from django.shortcuts import render


# Create your views here.

def index(request):
    blogList = BlogDetail.objects.order_by('-createTime')[:5]
    context = {'blogList': blogList}
    return render(request, 'blog/index.html', context)
