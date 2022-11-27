from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=50)
    Roll = serializers.IntegerField()
    Address  = serializers.CharField(max_length=50)
    
    def create(self,vaidated_data):
        return Student.objects.create(**vaidated_data)

    def update(self,instance,validated_data):
        instance.Name = validated_data.get('Name',instance.Name) 
        instance.Roll = validated_data.get('Roll',instance.Roll)
        instance.Address = validated_data.get('Address',instance.Address)
        instance.save()
        return instance