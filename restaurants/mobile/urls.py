from django.conf.urls import patterns, include, url
from restaurants.mobile.views import MenuView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurants.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^menu/$', MenuView.as_view(), name="menu_view"),
)
