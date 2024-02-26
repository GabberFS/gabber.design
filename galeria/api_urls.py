from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('rel/', views.MarcasView.as_view(), name='marcas'),
    path('marcas/', views.MarcasView.as_view(), name='marcas'),
    path('marca/delete/<int:pk>/', views.MarcaAPIViewDetail.as_view(), name='marca-delete'),
    path('marca/<int:pk>/', views.MarcaAPIViewDetail.as_view(), name='marca'),

    path('arquivos/', views.ArquivoAPIView.as_view(), name='arquivos'),
    path('arquivo/delete/<int:pk>/', views.ArquivoAPIViewDetail.as_view(), name='arquivo-delete'),
    path('arquivo/<int:pk>/', views.ArquivoAPIViewDetail.as_view(), name='arquivo'),


    path('publicacaos/', views.PublicacaoAPIView.as_view(), name='publicacaos'),
    path('publicacao/delete/<int:pk>/', views.PublicacaoAPIViewDetail.as_view(), name='publicacao-delete'),
    path('publicacao/<int:pk>/', views.PublicacaoAPIViewDetail.as_view(), name='publicacao'),
    path('publicacao/marca/<str:id>/', views.PublicacaoMarcaAPIViewDetail.as_view(), name='publicacao'),


    path('empresas/', views.EmpresaAPIView.as_view(), name='empresas'),
    path('empresa/delete/<int:pk>/', views.EmpresaAPIViewDetail.as_view(), name='empresa-delete'),
    path('empresa/<int:pk>/', views.EmpresaAPIViewDetail.as_view(), name='empresa'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
