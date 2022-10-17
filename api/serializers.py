from dataclasses import field
import imp
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Product, Country
from django.contrib.auth.models import User
