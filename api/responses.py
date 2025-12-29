from rest_framework.response import Response

class ResponseMixin():

    def success_response(self, data=None, status=200):
        return Response({
            'success': True,
            'status_code': status,
            'data': data,
        }, status=status)

    def error_response(self, code=None, message=None, status=400):
        return Response({
            'success': False,
            'status_code': status,
            'error':{
                'code': code,
                'message': message,
            }
        },status=status)