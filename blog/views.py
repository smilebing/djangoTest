from django.urls import reverse
from .models import BlogDetail
from .models import Article
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'blog/index.html', {'post_list': post_list})


def detail(request, id):
    try:
        blog = Article.objects.get(pk=id)
    except(KeyError, BlogDetail.DoesNotExist):
        return render(request, 'blog/detail.html', {
            'error_message': 'do not hava this blog'
        })
    else:
        context = {'post': blog}
        return render(request, 'blog/detail.html', context)


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/archives.html', {'post_list': post_list,
                                                  'error': False})


def about_me(request):
    return render(request, 'blog/aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'blog/index.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'blog/archives.html', {'post_list': post_list,
                                                              'error': True})
            else:
                return render(request, 'blog/archives.html', {'post_list': post_list,
                                                              'error': False})
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog:detail', args=[item.pk])
        # question = get_object_or_404(Question, pk=question_id)
        #     try:
        #         selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #     except (KeyError, Choice.DoesNotExist):
        #         # Redisplay the question voting form.
        #         return render(request, 'polls/detail.html', {
        #             'question': question,
        #             'error_message': "You didn't select a choice.",
        #         })
        #     else:
        #         selected_choice.votes += 1
        #         selected_choice.save()
        #         # Always return an HttpResponseRedirect after successfully dealing
        #         # with POST data. This prevents data from being posted twice if a
        #         # user hits the Back button.
        #         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
