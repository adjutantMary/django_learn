from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import PostSitemap

sitemaps = {
 'posts': PostSitemap,
}
urlpatterns = [
         path('admin/', admin.site.urls),
         path('app/', include('app.urls', "app")),
         path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

