from config import db
# models

class Activity(db.Model):
    __tablename__ = "activity"
    id = db.Column(db.Integer(),
                   primary_key=True)
    classcode = db.Column(db.String(256), nullable=False)
    student_id = db.Column(db.Integer(), nullable=False)
    score = db.Column(db.Integer())
    concluded = db.Column(db.Boolean(), default=False, nullable=False)

