from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [

    path('singup/', views.UserCreate.as_view(), name='registration'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('user_show/', views.UserShow.as_view(), name='user-show'),
    path('save_signals/', views.SaveSignalsShow.as_view(), name='save-signals'),
    path('profile/<int:pk>/', views.ChangeProfile.as_view(), name='my-profile'),

]
