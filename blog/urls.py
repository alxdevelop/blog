from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Home
    url(r'^$', 'simpleBlog.views.index', name="home"),
    url(r'^page/(?P<slug>[^\.]+)','pages.views.views_pages', name="views_pages"),
    url(r'^blog/post/(?P<slug>[^\.]+)', 'simpleBlog.views.view_post', name="view_blog_post"),
    url(r'^blog/categoria/(?P<slug>[^\.]+)', 'simpleBlog.views.view_category', name="view_blog_category"),

    url(r'^admin/', include(admin.site.urls)),
)
