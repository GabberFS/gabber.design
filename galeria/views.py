from datetime import datetime

from django.shortcuts import render

from galeria.models import publicacao, marca, arquivo, empresa, RelGaleria
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from galeria.serializers import MarcaSerializer, ArquivoSerializer, EmpresaSerializer, PublicacaoSerializer


def home(request):
    template_name = 'galeria/home.html'
    empresas = empresa.objects.all()

    pubs = publicacao.objects.all().filter(publicado=True).order_by('-data_criada')
    context = {
        'pubs': pubs,
        'empresas': empresas,
    }

    return render(request, template_name, context)


def pub_detail(request, pk):
    template_name = 'galeria/detail.html'

    try:
        pub = publicacao.objects.get(pk=pk)
        arquivos = arquivo.objects.all().filter(publicacao=pub).order_by('nome')
        try:
            rel = RelGaleria.objects.get(data_criada__month=datetime.now().month)
        except RelGaleria.DoesNotExist:
            rel = RelGaleria(data_criada=datetime.now())

        total_views = 0

        for obj in publicacao.objects.all():
            total_views += obj.views
            print(obj.views, total_views)

        rel.views_total = total_views
        rel.save()

        context = {
            'pub': pub,
            'arquivos': arquivos
        }
        pub.views += 1

        pub.save()
    except publicacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return render(request, template_name, context)


def marca_detail(request, pk):
    template_name = 'galeria/marca.html'

    try:
        obj = marca.objects.get(pk=pk)
        pubs = publicacao.objects.all().filter(marca=obj).order_by('-data_criada')
        context = {
            'marca': obj,
            'pubs': pubs
        }

    except marca.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return render(request, template_name, context)


class MarcasView(APIView):

    def get(self, request, format=None):
        obj = marca.objects.all()
        serializer = MarcaSerializer(obj, many=True)
        response = Response(serializer.data)
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:3000"

        return response

    def post(self, request, format=None):
        serializer = MarcaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MarcaAPIViewDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = marca.objects.get(pk=pk)
        except marca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MarcaSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            obj = marca.objects.get(pk=pk)
        except marca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArquivoAPIView(APIView):

    def get(self, request, format=None):
        obj = arquivo.objects.all().order_by('nome')
        serializer = ArquivoSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArquivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ArquivoAPIViewDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = arquivo.objects.get(pk=pk)
        except arquivo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArquivoSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            obj = arquivo.objects.get(pk=pk)
        except arquivo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicacaoAPIView(APIView):

    def get(self, request, format=None):
        obj = publicacao.objects.all()
        serializer = PublicacaoSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PublicacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PublicacaoAPIViewDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = publicacao.objects.get(pk=pk)
        except publicacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PublicacaoSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            obj = publicacao.objects.get(pk=pk)
        except publicacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicacaoMarcaAPIViewDetail(APIView):

    def get(self, request, id, format=None):
        obj = publicacao.objects.all().filter(marca=id)
        serializer = PublicacaoSerializer(obj, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            obj = publicacao.objects.get(pk=pk)
        except publicacao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmpresaAPIView(APIView):

    def get(self, request, format=None):
        obj = empresa.objects.all()
        serializer = EmpresaSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EmpresaAPIViewDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = empresa.objects.get(pk=pk)
        except empresa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            obj = empresa.objects.get(pk=pk)
        except empresa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
