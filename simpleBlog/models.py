from django.db import models
from django.db.models import permalink


# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  content = models.TextField()
  meta_description = models.CharField(max_length=250, null=True, blank=True)
  posted = models.DateField(auto_now_add=True)
  category = models.ForeignKey('Category')

  def __unicode__(self):
      return '%s' % self.title

  @permalink
  def get_absolute_url(self):
      return ('view_blog_post', None,{ 'slug' : self.slug })

class Category(models.Model):
  title = models.CharField(max_length=100, db_index=True)
  slug = models.SlugField(max_length=100, db_index=True)
  meta_description = models.CharField(max_length=250, null=True, blank=True)

  def __unicode__(self):
      return '%s' % self.title

  @permalink
  def get_absolute_url(self):
      return('view_blog_category', None,{ 'slug': self.slug })
