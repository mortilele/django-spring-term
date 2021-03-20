from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from users import views

urlpatterns = [
    # Your URLs...
    url(r'login/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'register/$', views.UserRegisterView.as_view(), name='register'),
    url(r'token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]