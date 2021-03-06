
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/instruments/',include('instruments.urls')),
    path('api/auth/', include('jwt_auth.urls')),
    path('api/conversations/', include('conversations.urls')),
    path('api/reviews/', include('reviews.urls')),
]
