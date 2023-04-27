from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="indexPage"),
    path("accounts/login/", views.signin, name="loginPage"),
    path("Signup", views.signup, name="signupPage"),
    path("home/", views.home, name="homePage"),
    path("logout/", views.logoutview, name="logoutPage"),
    path("menu/", views.menu, name="menuPage"),
    path("about/", views.about, name="aboutPage"),
   # path("profile/<str:username>/", views.profile, name="profilePage"),
   path("profile/", views.profile, name="profilePage"),
   path('food', views.menuFoodList, name="menuFoodPage"),
     path('drink', views.menuDrinkList, name="menuDrinkPage"),
      path('bakery', views.menuBakeryList, name="menuBakeryPage"),
   path('desert', views.menuDesertList, name="menuDesertPage"),
   #   path('menulist', views.menuList, name="menulistPage"),
   path('orderitem/<int:id>/', views.orderItem, name="orderPage",),


   ##password reset
 #  path('password_reset/', auth_views.PasswordResetView.as_view(template_name ="ForkAndKnife/forgotpass.html"),
  #       name='password_reset'),
            path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
