from application.errors import InvalidInputError

allowed_keys = ['bank_name', 'city', 'district', 'state', 'sort_by']


class Validator:
    @staticmethod
    def validate_search_input(data):
        if 'bank_name' not in data or 'state' not in data:
            raise InvalidInputError('Bank Name and State are required', 400)
        return {k: v for k, v in data.items() if k in allowed_keys}
