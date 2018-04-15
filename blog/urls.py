from django.urls import path,include
from .views import showBlogPage,detail

urlpatterns = [
    path("",showBlogPage,name='blog'),
    path('<int:blog_id>',detail,name='detail')
]