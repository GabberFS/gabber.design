from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacao/<int:pk>', views.pub_detail, name='pub_detail'),
    path('marca/<int:pk>', views.marca_detail, name='marca_detail'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
