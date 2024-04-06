from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Documents(Base):
    __tablename__ = 'documents'
    id: Mapped[int] = mapped_column(primary_key=True)
    psth: Mapped[str] = mapped_column(String(150))
    date: Mapped[datetime]


class DocumentText(Base):
    __tablename__ = 'document_text'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_doc: Mapped[int] = mapped_column(
        ForeignKey(
            'documents.id',
            ondelete='CASCADE',
        )
    )
    text: Mapped[str]
