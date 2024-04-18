from django.urls import path,include
from managementapp import views

urlpatterns = [
	path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact,name='contact'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name="about"),
    path('news',views.news,name='news'),



]

