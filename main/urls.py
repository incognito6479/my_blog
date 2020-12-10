from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('account/', views.my_account, name='account'),
    path('logout/', views.logout_user, name='logout'),
    path('img_upload/', views.upload, name='upload'),
    path('user_post/', views.show_user_post, name='user-post')
]