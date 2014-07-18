from django.shortcuts import render, render_to_response, get_object_or_404
from simpleBlog.models import *

# Create your views here.
def index(request):
  template = "index.html"
  posts = Post.objects.all().order_by('-id')[:5]
  categories = Category.objects.all()
  name_website = Website.objects.get(option = 'name')
  slogan_website = Website.objects.get(option = 'slogan')
  description_website = Website.objects.get(option = 'description')

  return render_to_response( template,{
    'name_website' : name_website.value,
    'title_website' : slogan_website.value,
    'description_website' : description_website.value,
    'categories' : categories,
    'posts' : posts
    })


def view_post(request, slug):
  template = "view_post.html"
  post = get_object_or_404(Post, slug=slug)
  name_website = Website.objects.get(option = 'name')
  description_website = post.meta_description

  return render_to_response( template,{
    'post' : post,
    'name_website' : name_website.value,
    'title_website' : post.title,
    'description_website' : description_website
    })


def view_category(request, slug):
  category = get_object_or_404(Category, slug=slug)
  posts = Post.objects.filter(category = category)[:10]
  name_website = Website.objects.get(option = 'name')
  template = "view_category.html"
  description_website = category.meta_description

  return render_to_response( template, {
    'category' : category,
    'posts' : posts,
    'name_website' : name_website.value,
    'title_website' : 'Categoria: ' + category.title,
    'description_website' : description_website
    })



