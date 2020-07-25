from django.urls import path, include
<<<<<<< HEAD
from .views import signup,login,shop_signup,shop_login,update_user
from registration import views
urlpatterns = [
    path('' ,views.signup , name="register"),
    path('login/' ,views.login, name="login" ),
    path('shop/' , views.shop_signup ,name="shopkeepersignup"),
    path('slogin/', views.shop_login , name="shopkeeperlogin"),
    path('update/', views.update_user, name="shopkeeperlogin")
=======
from .import views
urlpatterns = [
    path('' ,views.signup , name="register"),
    path('login/' ,views.login, name="login" ),
    path('shop/' , views.shop_signup ,name="shopkeepersignup")
    path('slogin', views)
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
]