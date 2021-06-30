from django.urls import path
from courses.api.views import CourseEnrollView
from . import views

app_name = "courses"
urlpatterns = [
    path("subjects/", views.SubjectListView.as_view(), name="subject_list"),
    path("subjects/<pk>/", views.SubjectDetailView.as_view(), name="subject_detail"),
    path('courses/<pk>/enroll/',CourseEnrollView.as_view(),name='course_enroll'),
]
