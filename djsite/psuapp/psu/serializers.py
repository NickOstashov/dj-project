from psu.models import Problem, FAQ
from rest_framework import serializers
from users.models import Applications, typeProblem

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()
    class Meta:
        model = FAQ
        fields = ['id', 'problem_id', 'question','answer','problem']


# class typeProblemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = typeProblem
#         fields = "__all__"
class ApplicationSerializer(serializers.ModelSerializer):
    get_status_display = serializers.CharField()
    kind_of_problem = ProblemSerializer()
    class Meta:
        model = Applications
        fields = "__all__"
        #fields.__add__('kind_of_problem ')