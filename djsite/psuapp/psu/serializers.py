from psu.models import Problem, FAQ
from rest_framework import serializers
from users.models import Applications

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
    class Meta:
        model = Applications
        fields = "__all__"