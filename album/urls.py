from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$',
        views.first_view,
        name='first_view'),
    url(r'^category/$',
        views.category,
        name='category_list'),
    url(r'^category/(?P<category_id>[0-9]+)/detail/$',
        views.category_detail,
        name='category_detail'),
    url(r'^photo/$',
       views.PhotoListView.as_view(),
       name='photo_list'),
    url(r'^photo/(?P<pk>[0-9]+)/detail/$',
        views.ProtoDetailView.as_view(),
        name='photo_detail'),
]
