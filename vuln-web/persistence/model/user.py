from sqlalchemy import Column, Identity, Integer, Sequence, String
from persistence.database import Base,DATABASE_KEYWORD

class User(Base):
    __tablename__ = f'{DATABASE_KEYWORD}_users'
    
    impenetrable_07062024_id = Column( Integer, Identity(start=1, cycle=True), primary_key=True)
    impenetrable_07062024_bio = Column(String(255), nullable=False)

