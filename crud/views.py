from django.shortcuts import render
from django.views.generic import TemplateView, ListView # 汎用ビューとリスト特化のビューをインポート
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 編集・更新・削除特化のビューをインポート
from .models import Product
from django.urls import reverse_lazy

# top.htmlを表示するためのビュー
class TopView(TemplateView):
    template_name = 'top.html'

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')