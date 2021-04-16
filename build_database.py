import os
from config import app, db, database_name
from models import Activity

# Data to initialize Database
ACTIVITIES = [
    {'classcode': '21E1_1', 'student_id': '1', 'concluded': False},
    {'classcode': '21E1_2', 'student_id': '1', 'concluded': False}
]

if os.path.exists(database_name):
    os.remove(database_name)


db.create_all()

for activity in ACTIVITIES:
    activity_obj = Activity(**activity)
    db.session.add(activity_obj)

db.session.commit()