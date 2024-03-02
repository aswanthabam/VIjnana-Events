from rest_framework.views import APIView
from utils.response import CustomResponse
from .serializers import ParticipantCreateSerializer

class InitializationView(APIView):
    def post(self, request):
        serializer = ParticipantCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(message="Initialization successful.", data=serializer.data).send_success_response()
        return CustomResponse(message="Initialization failed.", data=serializer.data).send_failure_response()