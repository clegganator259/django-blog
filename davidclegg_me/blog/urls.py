from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.post_list,name='post_list'),
        url(r'articles/(?P<post_title>[0-9a-zA-Z_!,?]+)',views.article),
        ]
