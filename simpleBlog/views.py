from django.shortcuts import render, render_to_response, get_object_or_404
from simpleBlog.models import Post, Category

# Create your views here.
def index(request):
  template = "index.html"
  posts = Post.objects.all().order_by('-id')[:5]
  categories = Category.objects.all()

  return render_to_response( template,{
    'categories' : categories,
    'posts' : posts
    })


def view_post(request, slug):
  template = "view_post.html"
  post = get_object_or_404(Post, slug=slug)
  return render_to_response( template,{
    'post' : post
    })


def view_category(request, slug):
  category = get_object_or_404(Category, slug=slug)
  posts = Post.objects.filter(category = category)[:10]
  template = "view_category.html"
  return render_to_response( template, {
    'category' : category,
    'posts' : posts
    })



