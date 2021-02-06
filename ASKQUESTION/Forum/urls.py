from django.urls import path,include
from . import views
 
urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('',views.home,name='home'),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
]