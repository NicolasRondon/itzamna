from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'image', 'interest')
