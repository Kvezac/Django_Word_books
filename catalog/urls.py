from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('edit/<int:id>/', views.edit1, name='edit1'),
    # path('create/', views.create, name='create'),
    # path('delete/', views.delete, name='delete'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
]
