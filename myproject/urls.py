"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views # アプリ内のviews.pyをインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name='top'), # TopViewをURLに紐付けてインスタンス化をルーティング
    path('crud/', views.ProductListView.as_view(), name='list'), # ProductListViewをURLに紐付けてインスタンス化をルーティング
    path('crud/new/', views.ProductCreateView.as_view(), name='new'),
]