from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("my_hh_app.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lk/', include("lk.urls"))

]
