from django.urls import path
from . import views

urlpatterns = [
    path('about/',  views.AboutTemplateView.as_view(),    name='about'),
    path('', views.GraphsListView.as_view(), name='graphs'),
    path('post/ajax/layout', views.post_layout,     name = "post_layout"),
]