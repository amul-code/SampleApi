from django.urls import path
from api import views


urlpatterns = [
    path('articles/', views.articleApi),
    path('createarticles/', views.createarticleApi),
    path('users/', views.usersApi),
    path('articleslist/', views.ArticlesListView.as_view()),
    path('articlesdetail/<int:pk>', views.ArticlesDetailView.as_view()),
]
