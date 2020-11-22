# from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class NewsView(generic.TemplateView):
    template_name = "news.html"

class ProductsView(generic.TemplateView):
    template_name = "products.html"

class ConceptView(generic.TemplateView):
    template_name = "concept.html"

class FaqView(generic.TemplateView):
    template_name = "faq.html"

class ShopView(generic.TemplateView):
    template_name = "shop.html"