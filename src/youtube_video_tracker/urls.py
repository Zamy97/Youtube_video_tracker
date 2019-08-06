from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import (
    home_page,
    login_form,
    add_song_form
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('login/', login_form),
    path('add_song/', add_song_form),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
