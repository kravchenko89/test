from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),

    path('auth/', include('django.contrib.auth.urls')),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),

]
