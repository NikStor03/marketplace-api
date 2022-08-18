from django.db.models import fields
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ('name', 'description')


class ProductShowListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductChangesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductChangesModel
        fields = (
            'name_was', 'name_new', 'description_was', 'description_new', 'start_date_was', 'start_date_new',
            'end_date_was', 'end_date_new', 'price_was', 'price_new')


class ProductPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ('price', 'start_date', 'end_date')
