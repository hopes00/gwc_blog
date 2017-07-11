from djanco.comf.urls import url
from . import views

urlpatterns= [
    url(r'^$', view.post_list, name= 'post_list'),
]
