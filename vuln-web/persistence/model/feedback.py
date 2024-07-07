from sqlalchemy import Column, Identity, Integer, String
from persistence.database import Base,DATABASE_KEYWORD

class Feedback(Base):
    __tablename__ = f'{DATABASE_KEYWORD}_feedbacks'
    
    impenetrable_07062024_id = Column( Integer, Identity(start=1, cycle=True), primary_key=True)
    impenetrable_07062024_message = Column(String(2048), nullable=False)

