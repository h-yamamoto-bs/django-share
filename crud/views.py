from django.shortcuts import render
from django.views.generic import TemplateView, ListView # 汎用ビューとリスト特化のビューをインポート
from django.views.generic.edit import CreateView # 編集特化のビューをインポート
from .models import Product

# top.htmlを表示するためのビュー
class TopView(TemplateView):
    template_name = 'top.html'

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
