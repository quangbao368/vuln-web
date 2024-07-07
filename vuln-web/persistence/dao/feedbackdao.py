
from persistence.database  import execute,DATABASE_KEYWORD
from persistence.model.feedback import Feedback
class FeedBackDao:
    def __init__(self) -> None:
        pass

    async def insert_feedback(self, msg:str):
        if msg is None:
            return
        query = f"INSERT INTO {DATABASE_KEYWORD}_feedbacks ({DATABASE_KEYWORD}_message) VALUES ('{msg}');"
        ret,msg =await execute(query)
        return ret,msg
    
    async def get_feedback_by_id(self, id:str):
        if id is None:
            return
        query = f"SELECT {DATABASE_KEYWORD}_message FROM {DATABASE_KEYWORD}_feedbacks WHERE {DATABASE_KEYWORD}_id = {id};"
        result,msg =await execute(query)
        if result:
            for row in result:
                return row,msg
        return None,msg
