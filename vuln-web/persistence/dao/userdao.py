
from persistence.database  import execute,DATABASE_KEYWORD
from persistence.model.user import User
class UserDao:
    def __init__(self) -> None:
        pass

    async def insert_user(self, bio:str):
        if bio is None:
            return
        query = f"INSERT INTO {DATABASE_KEYWORD}_users ({DATABASE_KEYWORD}_bio) VALUES ('{bio}');"
        ret,msg =await execute(query)
        return ret,msg
    
