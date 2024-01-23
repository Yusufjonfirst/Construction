from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from pages.views import home_pages_view, about_pages_view, contact_pages_view, blog_pages_view, project_pages_view, services_pages_view, single_pages_view

app_name = 'pages'

urlpatterns = [
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('about/', about_pages_view, name="about"),
    path('contact/', contact_pages_view, name="contact"),
    path('blog/', blog_pages_view, name="blog"),
    path('project/', project_pages_view, name="project"),
    path('services/', services_pages_view, name="services"),
    path('single/', single_pages_view, name="single"),
    path('', home_pages_view, name="home"),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
