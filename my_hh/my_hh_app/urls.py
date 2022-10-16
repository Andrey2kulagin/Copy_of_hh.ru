from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index,name='index'),
    path('resume_view/<int:pk>', views.resume_view,name='resume_view'),
    path('exit/', authViews.LogoutView.as_view(next_page='index'), name='exit'),
    path("send_resume", views.send_resume),
    path("registrations/<int:int_status>", views.registrations),
    path("add/skills", views.add_to_skills),
    path("vacancy_view/<int:id>", views.vacancy_view)
]
