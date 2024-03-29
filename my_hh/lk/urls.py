from django.urls import path
from . import views

urlpatterns = [
    path("", views.lk),
    path("resume_view/<int:pk>", views.resume_view),
    path('<int:pk>/update', views.resume_update),
    path('<int:pk>/change_company_info', views.change_company_info),
    path('<int:pk>/change_vacancy', views.change_vacancy),
    path('send_vacation', views.send_vacation),
    path('skills_for_check', views.skills_for_check),
    path('check_skill/<str:name>', views.check_skill),
]
