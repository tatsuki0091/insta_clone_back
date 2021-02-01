from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

# modelViewsetを設定するときに使用する
# modelViewset = モデルに対する、一覧取得、詳細取得、新規作成、更新、削除を
# 一括で作成してくれるもの
router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('', include(router.urls)),

]