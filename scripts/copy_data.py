import csv
import os

from application import db
from application.models import BankBranches

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
db.drop_all()
db.create_all()

with open(os.path.join(file_location, 'bank_branches.csv')) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        branch = BankBranches(**row)
        db.session.add(branch)
    db.session.commit()
