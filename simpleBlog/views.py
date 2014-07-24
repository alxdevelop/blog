from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.core.paginator import Paginator
from simpleBlog.models import *
from pages.models import Pages


def get_pages():
  return Pages.objects.all().order_by('orden')

def get_name_website():
  name_website = Website.objects.get(option = 'name')
  return name_website.value

def get_description_website():
  description_website = Website.objects.get(option = 'description')
  return description_website.value

def get_posts(numero, order=''):
  if numero == 0:
    return Post.objects.all().order_by(order+'id')
  else:
    return Post.objects.all().order_by(order+'id')[:numero]

def get_post(slug):
  return get_object_or_404(Post, slug=slug)

def get_categories():
  return Category.objects.all()

def get_category(slug):
  return get_object_or_404(Category, slug=slug)

def get_slogan_website():
  slogan = Website.objects.get(option = 'slogan')
  return slogan.value

def obtener_siguiente_pagina(pagina):
  pagina = int(pagina) + 1
  return pagina

def obtener_pagina_anterior(pagina):
  if int(pagina) > 1:
    pagina = int(pagina) - 1
  else:
    pagina = 1
  return pagina

def index(request):
  template = "index.html"
  posts = get_posts(5,'-')

  return render_to_response( template,{
    'name_website' : get_name_website,
    'slogan_website' : get_slogan_website,
    'title_website' : get_slogan_website,
    'description_website' : get_description_website,
    'categories' : get_categories,
    'pages' : get_pages,
    'posts' : posts
    }, RequestContext(request))


# Create your views here.
def blog(request, pagina = 1):
  template = "index.html"
  posts = get_posts(0,'-')
  p = Paginator(posts, 5)
  posts = p.page(pagina)

  return render_to_response( template,{
    'name_website' : get_name_website,
    'slogan_website' : get_slogan_website,
    'title_website' : get_slogan_website,
    'description_website' : get_description_website,
    'categories' : get_categories,
    'pages' : get_pages,
    'current_page': int(pagina),
    'next_page': obtener_siguiente_pagina(pagina),
    'prev_page': obtener_pagina_anterior(pagina),
    'posts' : posts
    }, RequestContext(request))


def view_post(request, slug):
  template = "view_post.html"
  post = get_post(slug) 
  description_website = post.meta_description
  slogan_website = Website.objects.get(option = 'slogan')

  return render_to_response( template,{
    'post' : post,
    'name_website' : get_name_website,
    'title_website' : post.title,
    'description_website' : description_website,
    'pages' : get_pages,
    'categories' : get_categories,
    'slogan_website' : slogan_website.value,
    }, RequestContext(request))


def view_category(request, slug):
  category = get_category(slug)
  posts = Post.objects.filter(category = category)[:10]
  template = "view_category.html"
  description_website = category.meta_description

  return render_to_response( template, {
    'category' : category,
    'categories' : get_categories,
    'posts' : posts,
    'name_website' : get_name_website,
    'title_website' : 'Categoria: ' + category.title,
    'pages' : get_pages,
    'description_website' : description_website
    }, RequestContext(request))



