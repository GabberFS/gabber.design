import uuid

from django.db import models
from django.utils.text import slugify


class empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    data_criada = models.DateTimeField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    site = models.URLField()
    instagram = models.URLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            # Gere o slug a partir do nome se não existir
            self.slug = slugify(self.nome)

            # Garanta que o slug é único, adicionando um número ao final, se necessário
            while empresa.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.nome) + '-' + str(uuid.uuid4())[:8]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class marca(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    data_criada = models.DateTimeField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)
    empresa = models.ForeignKey(empresa, on_delete=models.DO_NOTHING, null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    cor_1 = models.CharField(max_length=50, null=True, blank=True)
    cor_2 = models.CharField(max_length=50, null=True, blank=True)
    cor_3 = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Gere o slug a partir do nome se não existir
            self.slug = slugify(self.nome)

            # Garanta que o slug é único, adicionando um número ao final, se necessário
            while marca.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.nome) + '-' + str(uuid.uuid4())[:8]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class publicacao(models.Model):
    tipo = models.CharField(max_length=50, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    data_criada = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=False)
    data_atualizada = models.DateTimeField(auto_now=True)
    marca = models.ForeignKey(marca, on_delete=models.DO_NOTHING)
    img = models.URLField()
    tag = models.CharField(max_length=50, null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class arquivo(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    marca = models.ForeignKey(marca, on_delete=models.DO_NOTHING)
    publicacao = models.ForeignKey(publicacao, on_delete=models.DO_NOTHING)
    data_criada = models.DateTimeField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)
    url = models.URLField()
    tipo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome


class RelGaleria(models.Model):
    data_criada = models.DateTimeField()
    data_atualizada = models.DateTimeField(auto_now=True, null=True, blank=True)
    views_total = models.IntegerField(default=0)

    def __str__(self):
        ano = self.data_criada.year
        mes_escrito = self.data_criada.strftime('%B')
        return str(mes_escrito + ' ' + str(ano))
