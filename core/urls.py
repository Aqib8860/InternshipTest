from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('user-register/', UserRegistrationView.as_view(), name='user-register'),
    path('user-home', UserHomeView.as_view(), name='user-home'),
    path('user-logout', userLogout, name='user-logout'),

]
