from django.urls import path

from pypass import views

urlpatterns = [
    path('detail/<int:pk>', views.PyPassProfileUpdateView.as_view(), name='profile'),
    path('delete/<int:pk>', views.PyPassProfileDeleteView.as_view(), name='profile_delete')
]