"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('index/', views.index), #新增書本
    path('addbook/',views.add_book), #新增完成

    path('index_del/', views.index_del), #刪除書本
    path('delbook/',views.delete_book), #刪除完成

    path('index_update/', views.index_update), #編輯書本
    path('updatebook/',views.update_book), #編輯完成

    path('index_review/', views.addreview), #新增心得
    path('reviewbook/',views.add_review), #心得新增成功

    path('index_res/', views.resreview), #修改心得
    path('reviewbook/',views.res_review), #心得修改成功
    
    path('index_delreview/', views.delreview), #刪除心得
    path('delreviewbook/',views.del_review), #心得刪除成功

    path('index_search/', views.index_search), #搜尋作者
    path('searchauthor/',views.select_author), #作者呈現畫面

    path('orderby_a_y/',views.orderby_a_y), #搜尋書本依照作者年份升冪
    path('desc_a_y/',views.desc_a_y), #搜尋書本依照作者年份降冪

    path('index_regex/', views.index_regex), #關鍵字搜尋
    path('regex_search/',views.regex_search), #作者呈現畫面

    path('wrong/', views.wrong), # 資料不齊全頁面







]
