from django.urls import path
from . import views


app_name = 'myappcabahug'

urlpatterns = [
    
    path('', views.MyIndexView.as_view(), name="my_index_view"),
    path('signin/', views.MySignInView.as_view(), name="my_signin_view"),
    path('signup/', views.MySignUpView.as_view(), name="my_signup_view"),
]
