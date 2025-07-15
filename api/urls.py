
from django.urls import path
from . import views

urlpatterns = [
  
  path("api/resumes",views.ResumeAPIView.as_view()),
  path("api/resumes/<int:pk>",views.ResumeAPIView.as_view())

]