import datetime

from rest_framework import serializers

from galeria.models import marca, publicacao, arquivo, empresa, RelGaleria


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = marca
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(MarcaSerializer, self).to_representation(instance)
        pubs = publicacao.objects.all().filter(marca=instance)
        pubs_json = PublicacaoSerializer(pubs, many=True).data

        representation['pubs'] = pubs_json

        return representation


class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = arquivo
        fields = '__all__'


class RelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelGaleria
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = '__all__'


class PublicacaoSerializer(serializers.ModelSerializer):
    arquivos = ArquivoSerializer(many=True, read_only=True)

    class Meta:
        model = publicacao
        fields = ['id', 'views', 'titulo', 'data_criada', 'publicado', 'data_atualizada', 'marca', 'arquivos', 'img', 'tag', 'tipo']

    def to_representation(self, instance):
        representation = super(PublicacaoSerializer, self).to_representation(instance)
        representation['marca_self'] = {
            'id': instance.marca.id,
            'nome': instance.marca.nome
            # Adicione mais campos se necessário
        }


        arquivos = arquivo.objects.all().filter(publicacao=instance).order_by('-nome')
        arquivo_json = ArquivoSerializer(arquivos, many=True).data

        representation['arquivos'] = arquivo_json

        return representation
