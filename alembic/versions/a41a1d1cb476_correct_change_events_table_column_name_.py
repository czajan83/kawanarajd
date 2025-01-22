"""correct change events table column name: coffees_issued -> coffees_served

Revision ID: a41a1d1cb476
Revises: e4af93a12409
Create Date: 2025-01-22 11:05:06.814720

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a41a1d1cb476'
down_revision: Union[str, None] = 'e4af93a12409'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('coffees_served', sa.Integer(), nullable=True))
    op.drop_column('events', 'coffees_issued')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('coffees_issued', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('events', 'coffees_served')
    # ### end Alembic commands ###
