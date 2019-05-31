from django.conf.urls import include, url
from django.contrib import admin
from empapiapp import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'empapiro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^emp/',views.Emplist)
]
