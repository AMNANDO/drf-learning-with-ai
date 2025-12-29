from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "success": False,
            "error": {
                "status_code": response.status_code,
                "message": response.status_text,
                "detail": response.data,
            }
        }
        return response

class ProfileInActive(APIException):
    status_code = 403
    default_detail = "profile is inactive."
    default_code = "profile_inactive"