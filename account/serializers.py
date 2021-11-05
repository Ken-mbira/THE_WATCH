from rest_framework import serializers

from account.models import Account
from .emails import send_welcome_email

class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','username','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        """Defines what to do once a request having the new user data arrives
        """
        account = Account(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(self.validated_data['password'])
        send_welcome_email(account.username,account.email)

        account.save()
        return account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','username','date_joined','last_login',]