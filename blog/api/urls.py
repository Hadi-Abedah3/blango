from django.urls import path, include 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

#from blog.api.views import PostList, PostDetail
from rest_framework.authtoken import views
from .views import UserDetail, TagViewSet, PostViewSet

urlpatterns = [
    #path("posts/", PostList.as_view(), name="api_post_list"),
    #path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns += [ 
    path("", include(router.urls)),
]