from django.urls import path

from pypass import views

urlpatterns = [
    path('create', views.PyPassCreateLoginView.as_view(), name='create_login'),
    path('', views.PyPassListLoginView.as_view(), name='list_login'),
    path('detail/<int:pk>', views.PyPassDetailLoginView.as_view(), name='detail_login'),
    path('update/<int:pk>', views.PyPassUpdateLoginView.as_view(), name='update_login'),
    path('delete/<int:pk>', views.PyPassDeleteLoginView.as_view(), name='delete_login')
]
