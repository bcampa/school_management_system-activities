from config import ma
from models import Activity

class ActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Activity
        fields = ["id", "classcode", "student_id", "score", "concluded"]

class AllActivitiesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Activity
        fields = ["id", "classcode", "student_id", "score", "concluded"]

all_activities_schema = AllActivitiesSchema(many = True)
activity_schema = ActivitySchema()