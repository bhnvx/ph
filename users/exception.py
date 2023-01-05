from rest_framework import status


class AlreadyExistsError(Exception):
    status = status.HTTP_409_CONFLICT
    detail = "Already Exists."
