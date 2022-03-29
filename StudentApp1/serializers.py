from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import students

class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model = students
        fields = '__all__'