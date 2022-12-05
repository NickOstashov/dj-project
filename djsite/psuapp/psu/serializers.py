from psu.models import Problem, FAQ
from rest_framework import serializers

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()
    class Meta:
        model = FAQ
        fields = ['id', 'problem_id', 'question','answer','problem']