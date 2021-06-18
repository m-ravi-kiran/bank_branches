from application.errors import InvalidInputError

allowed_keys = ['bank_name', 'city', 'district', 'state', 'sort_by']


class Validator:
    @staticmethod
    def validate_search_input(data):
        """
        Validates the input
        Args:
            data: all the query parameters related to searching bank by name

        Returns:
            A valid set of keys and values to be used for searching the database table.
        """
        if 'bank_name' not in data or 'state' not in data:
            raise InvalidInputError('Bank Name and State are required', 400)
        return {k: v for k, v in data.items() if k in allowed_keys}
