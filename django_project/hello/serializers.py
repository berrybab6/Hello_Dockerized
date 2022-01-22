from hello.models import Hello
from rest_framework import serializers
# Serializers define the API representation.
class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hello
        fields = "__all__"