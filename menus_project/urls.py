from django.contrib import admin
from django.urls import path
from menus.views import menu_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:menu_name>',view=menu_view),
    path('',view=menu_view)
]
