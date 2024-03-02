from rest_framework import serializers
from db.models import Participant, Level

class ParticipantCreateSerializer(serializers.Serializer):
    current_order = serializers.IntegerField(read_only=True)
    participantId = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        p_id = Participant.objects.all().order_by('participantId').last()
        if p_id:
            p_id = p_id.participantId
        else:
            p_id = 0
        validated_data['current_order'] = 1
        validated_data['participantId'] = p_id + 1
        return Participant.objects.create(**validated_data)
    class Meta:
        fields =[
            'current_order',
            'participantId'
        ]
        model = Participant

class QuestionSerializer(serializers.Serializer):
    order = serializers.IntegerField(read_only=True)
    answer = serializers.CharField(required=True, write_only=True)
    question = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    difficulty = serializers.IntegerField(required=True)

    def create(self, validated_data):
        validated_data['order'] = Level.objects.all().count() + 1
        return Level.objects.create(**validated_data)
    class Meta:
        fields = [
            'order',
            'name',
            'question',
            'difficulty',
            'answer'
        ]
        model = Level
        WRITE_ONLY_FIELDS = ['answer']