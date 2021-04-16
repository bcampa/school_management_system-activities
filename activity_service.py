from nameko.rpc import rpc
import sqlite3

class DBConnection:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.con.row_factory = sqlite3.Row
        self.cursor = self.con.cursor()

    def __del__(self):
        self.con.close()

class ActivityService:
    name = "activity_service"
    db = DBConnection("activity.db")

    @rpc
    def hello_world(self):
        return "Hello World!"
    
    @rpc
    def get_activities(self):
        query = "SELECT * FROM activity;"
        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()
        return [{key: item[key] for key in item.keys()} for item in results]
    
    @rpc
    def get_activity(self, id):
        query = "SELECT * FROM activity WHERE id = ?;"
        self.db.cursor.execute(query, (id,))
        result = self.db.cursor.fetchone()
        return {key: result[key] for key in result.keys()}
    
    @rpc
    def conclude_activity(self, id):
        query = "UPDATE activity SET concluded = 1 WHERE id = ?;"
        self.db.con.execute(query, (id,))
        self.db.con.commit()
        return self.get_activity(id)
    
    @rpc
    def set_activity_conclusion(self, id, concluded):
        query = "UPDATE activity SET concluded = ? WHERE id = ?;"
        self.db.con.execute(query, (concluded, id))
        self.db.con.commit()
        return self.get_activity(id)
    
    @rpc
    def score_activity(self, id, score):
        query = "UPDATE activity SET score = ? WHERE id = ?;"
        self.db.con.execute(query, (score, id))
        self.db.con.commit()
        return self.get_activity(id)
    
    @rpc
    def add_activity(self, new_data):
        query = "INSERT INTO activity (classcode, student_id) VALUES (?, ?);"
        self.db.con.execute(query, (new_data['classcode'], new_data['student_id']))
        self.db.con.commit()
        return "OK"

        
        # unpacked_results = []
        # for item in results:
        #     unpacked_item = {}
        #     for key in item.keys():
        #         if key != "concluded":
        #             unpacked_item[key] = item[key]
        #         else:
        #             unpacked_item[key] = bool(item[key])
        #     unpacked_results.append(unpacked_item)
        # return unpacked_results