from django.contrib import admin
from .models import publicacao, arquivo, marca, empresa, RelGaleria

admin.site.register(RelGaleria)
admin.site.register(empresa)
admin.site.register(publicacao)
admin.site.register(arquivo)
admin.site.register(marca)
