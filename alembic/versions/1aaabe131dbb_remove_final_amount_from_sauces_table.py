"""remove final amount from sauces table

Revision ID: 1aaabe131dbb
Revises: dfc6c5a4fc01
Create Date: 2025-01-17 17:33:48.833204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '1aaabe131dbb'
down_revision: Union[str, None] = 'dfc6c5a4fc01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sauces', 'final_amount')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sauces', sa.Column('final_amount', mysql.FLOAT(), nullable=False))
    # ### end Alembic commands ###