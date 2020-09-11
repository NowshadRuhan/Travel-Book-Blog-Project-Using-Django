from django.urls import path
from App_Blog import views


app_name='App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view()  , name='blogList'),
    path('new-blog/', views.CreateBlog.as_view(), name='createBlog'),
    path('blog-details/<slug:slug>', views.blog_details, name='blogDetails'),
    path('like/<pk>/', views.liked, name='like'),
    path('unlike/<pk>/', views.unliked, name='unlike'),
    path('my-blog/', views.MyBlog.as_view(), name='myblog'),
    path('my-blog-edit/<slug:slug>/', views.UpdateBlog.as_view(), name='editBlog'),
]
