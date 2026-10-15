from rest_framework import serializers
from .models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

    def validate_nombre_articulo(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )
        return value

    def validate_cantidad(self, value):
        if value < 1 or value > 50:
            raise serializers.ValidationError(
                'La cantidad debe estar entre 1 y 50.'
            )
        return value

    def validate_nombre_donante(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )
        return value

    def validate_fono(self, value):
        if len(value) != 9:
            raise serializers.ValidationError(
                'El teléfono debe tener 9 dígitos.'
            )
        if not value.startswith('9'):
            raise serializers.ValidationError(
                'El teléfono debe empezar con 9.'
            )
        if not value.isdigit():
            raise serializers.ValidationError(
                'El teléfono solo debe contener números.'
            )
        return value
