from rest_framework.views import APIView
from utils.response import CustomResponse
from .serializers import ParticipantCreateSerializer, QuestionSerializer,SubmissionSerializer
from db.models import THParticipant, THLevel, THSubmission
from django.db.models import Count, F

class LeaderboardView(APIView):
    def get(self, request):
        subs = THSubmission.objects.all().order_by('-level','time')
        data = []
        ids = []
        for sub in subs:
            if sub.is_correct and sub.participantId.participantId not in ids:
                data.append({
                    "participantId":sub.participantId.participantId,
                    "name":sub.participantId.name,
                    "level":sub.level,
                    "time":sub.time,
                })
                ids.append(sub.participantId.participantId)
        return CustomResponse(message="Leaderboard fetched successfully.", data=data).send_success_response()
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
        participant = THParticipant.objects.filter(participantId=participantId).first()
        if not participant:
            return CustomResponse(message="Participant not found.").send_failure_response()
        level = participant.current_order
        last_question = THLevel.objects.all().order_by('order').last()
        last = False
        if last_question is None:
            last = True
        elif last_question.order < level:
            last = True
        if last:
            return CustomResponse(message="You have completed the game.", data={"won":True}).send_success_response()
        question = THLevel.objects.filter(order=level).first()
        serializer = QuestionSerializer(instance=question, many=False)
        return CustomResponse(message="Question fetched successfully.", data={"won":False,"data":serializer.data}).send_success_response()
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(message="Question added successfully.", data=serializer.data).send_success_response()
        return CustomResponse(message="Question addition failed.", data=serializer.errors).send_failure_response()

class SubmissionAPIView(APIView):
    def post(self, request):
        participantId = request.data.get('participantId')
        answer = request.data.get('answer')
        if not participantId:
            return CustomResponse(message="Participant ID not provided.").send_failure_response()
        if not answer:
            return CustomResponse(message="Answer not provided.").send_failure_response()
        participant = THParticipant.objects.filter(participantId=participantId).first()
        if not participant:
            return CustomResponse(message="Participant not found.").send_failure_response()
        submission = THSubmission.objects.create(
            participantId=participant,
            level=participant.current_order,
            value=answer,
            is_correct=False
        )
        sub_id = submission.submissionId
        print(sub_id)
        submission = THSubmission.objects.filter(submissionId=sub_id).first()
        level = participant.current_order
        last_question = THLevel.objects.all().order_by('order').last()
        last = False
        if last_question is None:
            last = True
        elif last_question.order < level:
            last = True
        if last:
            return CustomResponse(message="You have completed the game.", data={"won":True,"correct":True}).send_success_response()
        
        question = THLevel.objects.filter(order=level).first()
        if question.answer == answer:
            participant.current_order += 1
            participant.save()
            submission.is_correct = True
            submission.save()
            if last_question.order == level:
                return CustomResponse(message="You have completed the game.", data={"won":True,"correct":True}).send_success_response()
            return CustomResponse(message="Correct answer.", data={"correct":True,"won":False}).send_success_response()
        else:
            return CustomResponse(message="Incorrect answer.", data={"correct":False,"won":False}).send_success_response()