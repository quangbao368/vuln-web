
from persistence.dao.feedbackdao import FeedBackDao
from persistence.dao.userdao import UserDao

class DataAccessLayer():
    """This class is responsible for connecting to the database and executing queries"""

    def __init__(self):
        self.db_services = dict()
        self.db_services["feedback"] = FeedBackDao()
        self.db_services['user'] =UserDao()

    # FLOW DAL
   

    async def insert_feedback(self, msg:str):
        service = self.db_services["feedback"]
        ret,msg =await service.insert_feedback(msg)
        return ret,msg
    
    async def get_feedback_by_id(self, msg:str):
        service = self.db_services["feedback"]
        ret,msg =await service.get_feedback_by_id(msg)
        return ret,msg
    
    async def insert_user(self, bio:str):
        service = self.db_services["user"]
        ret,msg =await service.insert_user(bio)
        return ret,msg

DAL = DataAccessLayer()
