"""mydbproject URL Configuration

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
from django.urls import path
from myappcabahug import views
app_name = 'myappcabahug'

urlpatterns = [
    path('', views.MyIndexView.as_view(), name="my_index_view"),
    path('signin/', views.MySignInView.as_view(), name="my_signin_view"),
    path('signup/', views.MySignUpView.as_view(), name="my_signup_view"),
    path('dashboard/', views.MyDashBoardView.as_view(), name="my_dashboard_view"),
    path('tables/', views.MyTablesView.as_view(), name="my_tables_view"),
    path('reservation/', views.MyReservationView.as_view(), name="my_appointment_view"),
    path('admin/', admin.site.urls),
    path('logout', views.MyLogoutView.as_view(), name='logout'),

]
