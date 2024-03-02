from rest_framework import serializers
from db.models import Participant

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