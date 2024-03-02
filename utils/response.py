from rest_framework.response import Response

class CustomResponse:
    def __init__(self, message, data=None):
        self.message = message
        self.data = data

    def send_success_response(self,status:int = 200):
        return Response({
            'status': 'success',
            'message': self.message,
            'data': self.data
        },status=status)

    def send_failure_response(self,status:int = 400):
        return Response({
            'status': 'failure',
            'message': self.message,
            'data': self.data
        },status=status)
