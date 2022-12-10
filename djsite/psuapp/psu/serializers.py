from psu.models import Problem, FAQ
from rest_framework import serializers
from users.models import Applications, CustomUser

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"

class FaqSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()
    class Meta:
        model = FAQ
        fields = ['id', 'problem_id', 'question','answer','problem']


class ApplicationSerializer(serializers.ModelSerializer):
    #get_status_display = serializers.CharField()
    class Meta:
        model = Applications
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='id')
    user_name = serializers.CharField(source='username')
    class Meta:
        model = CustomUser
        fields = ['user_id', 'user_name',]