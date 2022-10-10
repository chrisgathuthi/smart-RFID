from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from security.settings import DEBUG
from . import views

app_name = "generator"
urlpatterns = [
    path("",views.IndexTemplate.as_view(), name="index-page"),
] 
htmx_patterns = [
    path("form-data",views.FormData.as_view(),name="form-data")
]
urlpatterns += htmx_patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)