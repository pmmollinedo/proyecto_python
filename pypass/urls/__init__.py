from django.urls import path, include

app_name = 'pypass'

urlpatterns = [
    path('auth/', include('pypass.urls.auth_urls')),
    path('logins/', include('pypass.urls.saved_login_urls')),
    #path('endpoint/', include('pypass.urls.endpoints_urls'))
]
