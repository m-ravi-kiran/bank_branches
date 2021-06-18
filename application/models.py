from application import db
from application.serializer import Serializer


class BankBranches(db.Model, Serializer):
    ifsc = db.Column(db.String(20), primary_key=True)
    bank_id = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    district = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), index=True, nullable=False)
    bank_name = db.Column(db.String(30), index=True, nullable=False)

    def __str__(self):
        return f'bank_id = {self.bank_id}, ifsc = {self.ifsc}'

    @property
    def serialize(self):
        obj = Serializer.serialize(self)
        return obj
