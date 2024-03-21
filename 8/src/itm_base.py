from datetime import date, datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core import Base


class Providers(Base):
    code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        comment="provider code",
    )
    name_provider: Mapped[str | None] = mapped_column(
        String(50),
        comment="provider name",
    )
    pred_provider: Mapped[str | None] = mapped_column(
        String(50),
        comment="supplier's representative",
    )
    asked: Mapped[str | None] = mapped_column(
        String(50),
        comment="name to contact",
    )
    address: Mapped[str | None] = mapped_column(
        String(150),
        comment="address to provider",
    )
    delivery: Mapped[list["Delivery"]] = relationship(back_populates="provider")


class Delivery(Base):
    code: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        comment="code delivery",
    )
    date_delivery: Mapped[date | None] = mapped_column(
        comment="date delivery",
    )
    provider_id: Mapped[int | None] = mapped_column(
        ForeignKey("d_providers.id"),
        comment="id to provider",
    )
    provider: Mapped["Providers"] = relationship(back_populates="delivery")
    products: Mapped[list["Products"]] = relationship(back_populates="delivery")


class Emploers(Base):

    code: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        comment="code employee",
    )
    firstname: Mapped[str | None] = mapped_column(
        String(50),
        comment="first name employee",
    )
    surname: Mapped[str | None] = mapped_column(
        String(50),
        comment="surname name employee",
    )
    lastname: Mapped[str | None] = mapped_column(
        String(50),
        comment="lastname name employee",
    )
    jobtitle: Mapped[str | None] = mapped_column(
        String(50),
        comment="jobtitle employee",
    )
    address: Mapped[str | None] = mapped_column(
        String(150),
        comment="address to employee",
    )
    phone: Mapped[str | None] = mapped_column(
        String(15),
        comment="phone to employee",
    )
    birthday: Mapped[date | None] = mapped_column(
        nullable=False,
        comment="birthdate to employee",
    )
    orders: Mapped[list["Orders"]] = relationship(back_populates="emploer")


class Products(Base):
    code: Mapped[str | None] = mapped_column(
        String(50), unique=True, comment="product code"
    )
    name: Mapped[str | None] = mapped_column(String(150), comment="name product")
    description: Mapped[str | None]
    cost_buy: Mapped[int | None]
    is_existed: Mapped[bool | None]
    cnt: Mapped[int | None]
    cost_sell: Mapped[int | None]
    delivery_id: Mapped[int | None] = mapped_column(
        ForeignKey("d_delivery.id"),
        comment="id row for delivery",
    )

    delivery: Mapped["Delivery"] = relationship(back_populates="products")
    orders: Mapped["Orders"] = relationship(back_populates="products")


class Orders(Base):
    code: Mapped[str | None] = mapped_column(String(30), comment="code order")
    date_placed: Mapped[date | None] = mapped_column(default=datetime.now)
    date_executed: Mapped[date | None] = mapped_column(comment="test")
    client_id: Mapped[int | None] = mapped_column(
        ForeignKey("d_client.id"),
        comment="href of client",
    )
    emploer_id: Mapped[int | None] = mapped_column(
        ForeignKey("d_emploers.id"),
        comment="href of order",
    )
    product_id: Mapped[int | None] = mapped_column(
        ForeignKey("d_products.id"),
        comment="href of product",
    )

    client: Mapped["Client"] = relationship(back_populates="orders")
    emploer: Mapped["Emploers"] = relationship(back_populates="orders")
    products: Mapped["Products"] = relationship(back_populates="orders")


class Client(Base):
    fio: Mapped[str] = mapped_column(String(150), comment="full name client")
    address: Mapped[str] = mapped_column(
        String(150),
        comment="Client address for life",
    )
    phone: Mapped[str] = mapped_column(String(15), comment="phone client")
    orders: Mapped[list["Orders"]] = relationship(back_populates="client")
