from datetime import date
from sqlalchemy import select, and_, or_
from sqlalchemy.orm import selectinload, noload
from core import get_session

from itm_base import (
    Client,
    Products,
    Emploers,
    Delivery,
    Providers,
    Orders,
)

# with session_local() as session:

session = get_session()

query = None
res = None


def execute_(query):
    obj = session.execute(query)
    return obj.scalars().all()


# res = Providers(
#     code="543",
#     name_provider="aliexpress",
#     pred_provider="Antio",
#     asked="Antio",
#     address="street",
# )

# res = Emploers(
#     code="154",
#     firstname="john",
#     surname="Ern",
#     phone="8912341231",
#     birthday=date(1999, 1, 4),
#     jobtitle="managers",
# )

res = Delivery(code="", date_delivery=date(2023, 4, 2), provider_id=1)

session.add(res)
session.commit()
session.refresh(res)


query = select(Delivery)
print(execute_(query))
