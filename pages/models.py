from django.db import models
from django.db.models import permalink

# Create your models here.
class Pages(models.Model):
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  body = models.TextField()
  meta_description = models.CharField(max_length=250, null=True, blank=True)
  orden = models.IntegerField(default=0)
  posted = models.DateField(auto_now_add=True)

  def __unicode__(self):
    return '%s' % self.title

  @permalink
  def get_absolute_url(self):
    return ('views_pages', None,{'slug': self.slug })
