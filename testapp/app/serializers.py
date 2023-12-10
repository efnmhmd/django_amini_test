from rest_framework import serializers
from .models import *
class PersonSerializer( serializers.Serializer):
    lname = serializers.CharField(max_length=6)
    fname = serializers.CharField(max_length=6)
    # created = serializers.DateTimeField()
    # updated = serializers.DateTimeField()
    active = serializers.BooleanField()

    def validate_lname(self, value):
        """
        Check that the blog post is about Django.
        """
        print(value)
        if value[0] != "e":
            raise serializers.ValidationError("Ghalat kardi")
        return value
class PhoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields ="__all__"

class PersonModelSerializer(serializers.ModelSerializer):
    # phones = PhoneModelSerializer(many=True)
    class Meta:
        model = Person
        fields = ["id","lname","fname","active","created","phones"]
        read_only_fields = ['active']
    def create(self,validated_data):
        print("IM in create")
        print(validated_data)
        return validated_data
    
    def update(self,instance,validated_data):
        print("IM in update")
        print(validated_data)
        print(instance)
        return validated_data