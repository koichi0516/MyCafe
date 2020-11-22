from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('news/', views.NewsView.as_view(), name="news"),
    path('products/', views.ProductsView.as_view(), name="products"),
    path('concept/', views.ConceptView.as_view(), name="concept"),
    path('faq/', views.FaqView.as_view(), name="faq"),
    path('shop/', views.ShopView.as_view(), name="shop"),
]