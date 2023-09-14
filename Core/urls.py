"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    # re_path(r"^jet/", include("jet.urls", "jet")),
    path("", include("shop.urls")),
    path("admin/", admin.site.urls),
    re_path(r"^chaining/", include("smart_selects.urls")),
    re_path(r"^_nested_admin/", include("nested_admin.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = _("Artmart Admin")  # Change this to your desired admin title.
admin.site.site_header = _("Artmart")  # Change this to your desired admin header.
admin.site.index_title = _(
    "Artmart | Dashboard"
)  # Change this to your desired index title.
