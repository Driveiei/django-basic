from django.contrib import admin
from django.urls import path
from application.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    #test view line 6
    path('', IndexView),
]
