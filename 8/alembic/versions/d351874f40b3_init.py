"""init

Revision ID: d351874f40b3
Revises: 
Create Date: 2024-03-20 00:33:41.090295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd351874f40b3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employers',
    sa.Column('code_emp', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('jobtitle', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###off


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employers')
    # ### end Alembic commands ###
