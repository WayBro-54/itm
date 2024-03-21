from typing import Dict, Any

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session,
    declared_attr,
    Mapped,
    mapped_column,
)
from sqlalchemy import create_engine

from config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return "d_" + cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

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

engine = create_engine(
    settings.db.url,
    echo=settings.db.echo,
    # future=settings.db.future,
)

engine.connect()

session_local = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
)


def get_session() -> Session:
    with session_local() as session_:
        return session_
