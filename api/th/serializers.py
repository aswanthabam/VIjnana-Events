from rest_framework import serializers
from db.models import THParticipant, THLevel, THSubmission

class SubmissionSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True, source='participantId.name')
    level = serializers.IntegerField(required=True)
    time = serializers.DateTimeField(read_only=True)
    is_correct = serializers.BooleanField(read_only=True)
    
    class Meta:
        fields = [
            # 'name',
            'level',
            'time',
            'is_correct'
        ]
        model = THSubmission

class ParticipantCreateSerializer(serializers.Serializer):
    current_order = serializers.IntegerField(read_only=True)
    participantId = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    def create(self, validated_data):
        p_id = THParticipant.objects.all().order_by('participantId').last()
        if p_id:
            p_id = p_id.participantId
        else:
            p_id = 0
        validated_data['current_order'] = 1
        validated_data['participantId'] = p_id + 1
        return THParticipant.objects.create(**validated_data)
    class Meta:
        fields =[
            'name',
            'current_order',
            'participantId'
        ]
        model = THParticipant

class QuestionSerializer(serializers.Serializer):
    order = serializers.IntegerField(read_only=True)
    answer = serializers.CharField(required=True, write_only=True)
    question = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    difficulty = serializers.IntegerField(required=True)

    def create(self, validated_data):
        validated_data['order'] = THLevel.objects.all().count() + 1
        return THLevel.objects.create(**validated_data)
    class Meta:
        fields = [
            'order',
            'name',
            'question',
            'difficulty',
            'answer'
        ]
        model = THLevel
        WRITE_ONLY_FIELDS = ['answer']