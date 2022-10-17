from rest_framework import serializers
from.models import Matricula
from.models import Alumno

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Matricula
        fields="__all__"

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alumno
        fields="__all__"
