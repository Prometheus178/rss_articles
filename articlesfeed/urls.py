from django.urls import path
from django.conf.urls import url
from articlesfeed import views

app_name = 'articlesfeed'

urlpatterns = [
    path('', views.EKnowledgeIndex.as_view(), name='index'),
    path('<slug:section>/', views.ESectionView.as_view(), name='section'),
    path('<slug:section>/<int:article_id>/', views.EArticleView.as_view(), name='article'),
    
]
