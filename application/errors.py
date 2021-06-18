class ApiException(Exception):
    """Exception for raising exceptions for APIs."""

    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


class InvalidInputError(ApiException):
    pass
