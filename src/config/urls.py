from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/academic/', include('academic.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/content/', include('content.urls')),
    path('api/assignments/', include('assignments.urls')),
    path('api/evaluations/', include('evaluations.urls')),
    path('api/forums/', include('forums.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)