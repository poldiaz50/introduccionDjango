
from django.contrib import admin
from django.urls import include, path
from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("blog/", include("blog.urls", namespace="blog")),
    path("__reload__/", include("django_browser_reload.urls")),
]
