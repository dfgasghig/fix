from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, RateView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('search_things', views.SearchPosts, name = 'search_things'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name = 'delete_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('category/<str:cats>', CategoryView, name = 'category'),
    path('category-list', CategoryListView, name = 'category-list'),
    path('article/<int:pk>/rate_post/', RateView, name = 'rate_post'),
]

