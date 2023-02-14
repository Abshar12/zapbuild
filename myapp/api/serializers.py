from rest_framework import serializers
from myapp.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','is_client']

class ManagerSignupSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match.Please check and try again"})
        user.set_password(password)
        user.is_manager=True
        user.save()
        Manager.objects.create(user=user)
        return user


class ClientSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model = User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self,**kwargs):
        user=User(
        username=self.validated_data['username'],
        email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match.Please check and try again"})
        user.set_password(password)
        user.is_client=True
        user.save()
        Client.objects.create(user=user)
        return user


class EmployeeSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self,**kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match.Please check and try again"})
        user.set_password(password)
        user.is_employee=True
        user.save()
        Employee.objects.create(user=user)
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields="__all__"