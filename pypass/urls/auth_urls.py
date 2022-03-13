from django.urls import path

from pypass.views import auth_views

urlpatterns = [
    path('login', auth_views.PyPassLoginView.as_view(), name='login'),
    path('register', auth_views.PyPassRegisterView.as_view(), name='register'),
    path('logout', auth_views.PyPassLogoutView.as_view(), name='logout')
]
