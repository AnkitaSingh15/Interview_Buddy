"""Interview_Buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hackathon.views import *

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_job_role/', get_job_role),
    path('get_candidate_details/', get_candidate_details),
    path('get_candidate_interview_details/', get_candidate_interview_details),
    path('get_transcript_questions/', get_transcript_questions),
    path('save_questions/', save_questions),
    path('get_roadmap_data/', get_roadmap_data),
    path('get_suggestion/', get_suggestion)

]
