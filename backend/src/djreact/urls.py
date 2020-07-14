from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
	#path(r'^api-auth/', include('rest_framework.urls')),
	path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('articles.api.urls')),
    #path('', include('articles.urls')),
    
]

#path('api-auth/', include('rest_framework.urls')),