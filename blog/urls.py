from django.conf.urls import url
from . import views
"""   Module contains  URL partterns for the blocj and imported in
the  mysite/urls.py 'url(r'', include('blog.urls'))' to keep code clean"""

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
