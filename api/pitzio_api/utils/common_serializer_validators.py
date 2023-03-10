from rest_framework import serializers


def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError("This field must be an even number.")
