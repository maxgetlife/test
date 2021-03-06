from django.urls import path

from . import views

app_name = 'futureblog' \
           ''
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:futureblog_id>/', views.detail, name = 'detail'),
    path('<int:futureblog_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
