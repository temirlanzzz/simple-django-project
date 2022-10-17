from dataclasses import field
import imp
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Product, Country
from django.contrib.auth.models import User
import base64
from django.utils.html import format_html
from django.utils.safestring import mark_safe
class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ["id","name","price","quantity","country","city","address", "post_date","description","subcategory","image","user"]

class CountrySerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = Country
        fields = ('id', 'name')