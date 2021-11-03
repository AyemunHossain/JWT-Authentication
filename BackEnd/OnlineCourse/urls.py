from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls'))
    path('', include('CourseManagement.urls')),
    #path('api-auth/', include('rest_framework.urls'))
    path('token-auth/', obtain_jwt_token)
]