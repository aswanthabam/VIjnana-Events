from rest_framework.views import APIView
from utils.response import CustomResponse
from .serializers import ParticipantCreateSerializer, QuestionSerializer
from db.models import Participant, Level

class InitializationView(APIView):
    def post(self, request):
        serializer = ParticipantCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(message="Initialization successful.", data=serializer.data).send_success_response()
        return CustomResponse(message="Initialization failed.", data=serializer.errors).send_failure_response()

class QuestionAPIView(APIView):

    def get(self, request):
        participantId = request.GET.get('participantId')
        if not participantId:
            return CustomResponse(message="Participant ID not provided.").send_failure_response()
        participant = Participant.objects.filter(participantId=participantId).first()
        if not participant:
            return CustomResponse(message="Participant not found.").send_failure_response()
        level = participant.current_order
        last_question = Level.objects.all().order_by('order').last()
        last = False
        if last_question is None:
            last = True
        elif last_question.order == level:
            last = True
        if last:
            return CustomResponse(message="You have completed the game.", data={"won":True}).send_failure_response()
        question = Level.objects.filter(order=level).first()
        serializer = QuestionSerializer(instance=question, many=False)
        return CustomResponse(message="Question fetched successfully.", data=serializer.data).send_success_response()
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(message="Question added successfully.", data=serializer.data).send_success_response()
        return CustomResponse(message="Question addition failed.", data=serializer.errors).send_failure_response()
