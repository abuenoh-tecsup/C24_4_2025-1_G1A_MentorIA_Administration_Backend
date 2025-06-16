from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-django/auth/', include('authentication.urls')),
    path('api-django/academic/', include('academic.urls')),
    path('api-django/courses/', include('courses.urls')),
    path('api-django/content/', include('content.urls')),
    path('api-django/assignments/', include('assignments.urls')),
    path('api-django/evaluations/', include('evaluations.urls')),
    path('api-django/forums/', include('forums.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)