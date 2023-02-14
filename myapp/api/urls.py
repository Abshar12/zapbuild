from django.urls import path
from myapp.api.views import *
from django.urls import include, re_path

urlpatterns=[
    path('',hello),
    path('signup/client/',ClientSignupView.as_view()),
    path('signup/manager/',ManagertSignupView.as_view()),
    path('signup/employee/',EmploeeSignupView.as_view()),
    path('task',task_api),
    path('task/([0-9]+)/',task_api)
    
    

]