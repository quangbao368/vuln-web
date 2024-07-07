import logging
import os
import secrets
import string
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError,SQLAlchemyError
from sqlalchemy import MetaData, text
from sqlalchemy.orm.session import Session

from defination import DATABASE_KEYWORD




Base = declarative_base()



metadata = MetaData()

# Update the connection string for PostgreSQL
engine = create_async_engine(
    f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}",
    echo=False,
)



init = False


async def initialize():
    from sqlalchemy.exc import OperationalError
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.create_all)
            FLAG=generate_random_string(20)
            await conn.execute(text(f"INSERT INTO {DATABASE_KEYWORD}_users ({DATABASE_KEYWORD}_bio) VALUES ('{(FLAG)}');"))
        except OperationalError as e:
            _LOGGER.warn(f"{str(e)}")
        

async def db_session() ->Session:
    #if not init:
    #    await initialize()
    #    init = True
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

_LOGGER = logging.getLogger(__name__)

async def execute(query):
    async_session = await db_session()
    msg = None
    try:
        async with async_session() as session:
            async with session.begin():
                result = await session.execute(text(query))  
                await session.commit()
                return result,msg
    except ProgrammingError as e:
        # Handle any errors if needed
        _LOGGER.warning(str(e))
        await session.rollback()
        msg=f"Database error: {str(e)}"
    except SQLAlchemyError as e:
        _LOGGER.warning(str(e))
        await session.rollback()
        msg=f"Database error: {str(e)}"

    return None,msg



def generate_random_string(length=16):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

