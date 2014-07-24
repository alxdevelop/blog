from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
from pages.models import *
from simpleBlog.views import *
from simpleBlog.models import Website


def get_page(slug):
  return get_object_or_404(Pages, slug=slug)


# Create your views here.
def views_pages(request, slug):
  template = "views_pages.html"
  pages = get_pages
  page = get_page(slug)
  name_website = Website.objects.get(option = 'name')
  description_website = page.meta_description
  slogan_website = Website.objects.get(option = 'slogan')

  return render_to_response( template, {
    'page' : page,
    'pages' : get_pages,
    'categories' : get_categories,
    'name_website' : name_website.value,
    'title_website' : page.title,
    'description_website' : description_website,
    'slogan_website' : slogan_website.value,
    }, RequestContext(request))
