from typing import Dict, Any

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from .config import settings


class PreBase:

    def __repr__(self) -> str:
        params = ", ".join(
            f"{attr}={value!r}"
            for attr, value in self.__dict__.items()
            if not attr.startswith("_")
        )
        return f"{type(self).__name__}({params})"

    def as_dict(self) -> Dict[str, Any]:
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith("_")
        }


Base = declarative_base(cls=PreBase)


engine = create_async_engine(settings.db_url, echo=True, future=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
