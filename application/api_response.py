class ApiResponse:
    """Class to send the API responses."""

    @staticmethod
    def get_error_response(message='Internal Server Error', status_code=500):
        """Returns the error response.
        Args:
            message: error message to be used in the response
            status_code: HTTP status code

        Returns:
            A tuple with first element containing of response object and the second element containing the HTTP
            status code.
        """
        payload = {'status': status_code, 'result': message}
        return payload, status_code

    @staticmethod
    def get_success_response(result):
        """Returns the success response.

        Args:
            result: the final sum.

        Returns:
            A tuple with first element containing of response object and the second element containing the HTTP
            status code.
        """
        payload = {'status': 200, 'result': result}
        return payload, 200
