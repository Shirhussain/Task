from django.contrib import admin
from django.urls import path
from shirdo.views import home, delete, cross_off, uncross, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('delete/<int:task_id>/', delete, name="delete"),
    path('cross_off/<int:task_id>/', cross_off, name="cross_off"),
    path('uncross/<int:task_id>/', uncross, name="uncross"),
    path('edit/<int:task_id>/', update, name="edit"),
]
