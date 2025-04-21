from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Category


# Create your views here.
def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    print(posts)
    context = {
        'post_list': posts
    }

    templates = 'blog/index.html'
    return render(request, templates, context)


def post_detail(request, id):

    post = get_object_or_404(Post, id=id)

    if not post.is_published:
        raise Http404()

    if post.pub_date > timezone.now():
        raise Http404()

    if post.category and not post.category.is_published:
        raise Http404()

    template = 'blog/detail.html'
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    if not category.is_published:
        raise Http404("Категория не опубликована.")

    current_time = timezone.now()

    post = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    )
    template = 'blog/category.html'

    context = {
        'category': category,
        'post_list': post
    }

    return render(request, template, context)
