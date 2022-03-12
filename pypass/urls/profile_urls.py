from django.urls import path

from pypass import views

urlpatterns = [
    path('detail/<int:pk>', views.PyPassProfileUpdateView.as_view(), name='profile')
]