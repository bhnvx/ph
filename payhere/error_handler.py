import traceback

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from users.exception import AlreadyExistsError


def custom_exception_handler(exc, context):
    # logging exception
    print("\033[91m")
    traceback.print_exc()
    print("\033[0m")

    # handling exception
    if isinstance(exc, NotImplementedError):
        return Response(
            {"error": "not implemented yet"}, status=status.HTTP_501_NOT_IMPLEMENTED
        )
    elif isinstance(exc, serializers.ValidationError):
        return Response(
            {"error": "serializer validation failed"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    elif isinstance(exc, AlreadyExistsError):
        return Response(
            {"error": AlreadyExistsError.detail}, status=AlreadyExistsError.status
        )

    # default exception handler
    return exception_handler(exc, context)
