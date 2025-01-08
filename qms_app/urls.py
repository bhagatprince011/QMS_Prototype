from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('contractor/<int:road_id>/', views.contractor, name='contractor'),
    path('engineer/<int:road_id>/', views.engineer, name='engineer'),
    path('administrator/<int:road_id>/', views.administrator, name='administrator'),
    path('upload/', views.upload_file, name='upload_file'),
    path("download-sample/", views.download_sample, name="download_sample"),
    path('download-evidence/<int:road_id>/', views.downloadEvidence, name='download_evidence'),
    path('sendRemarks/', views.sendRemarks, name='sendRemarks'),
    path('approve/', views.approve, name='approve'),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

