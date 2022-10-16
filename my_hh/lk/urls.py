from django.urls import path
from . import views

urlpatterns = [
    path("", views.lk),
    path("resume_view/<int:pk>", views.resume_view),
    path('<int:pk>/update', views.NewUpdateView.as_view()),
    path('<int:pk>/change_company_info', views.CompanyUpdate.as_view()),
    path('send_vacation', views.send_vacation),
]
