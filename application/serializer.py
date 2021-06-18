from flask_sqlalchemy import inspect


class Serializer:
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(li):
        return [m.serialize for m in li]
