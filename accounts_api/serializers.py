from rest_framework import serializers
from accounts.models import Account


# class LoginSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Account
# 		fields = ['email', 'password',]

# 		extra_kwargs = {'password': {'write_only': True}}

# 	def validate(self, data):
# 		password = data.get('password')
# 		email = data.get('email')


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):

        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class AccountRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username']


class ChangePasswordSerializer(serializers.ModelSerializer):
    cpassword = serializers.CharField(write_only=True, required=True)
    cpassword2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ['cpassword', 'cpassword2', ]

    def validate(self, attrs):
        if attrs['cpassword'] != attrs['cpassword2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['cpassword'])
        instance.save()
        return instance
