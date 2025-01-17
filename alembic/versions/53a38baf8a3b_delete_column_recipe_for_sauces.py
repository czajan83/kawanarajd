"""delete column Recipe for Sauces

Revision ID: 53a38baf8a3b
Revises: 1c97dcc94f1b
Create Date: 2025-01-17 15:16:28.045926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '53a38baf8a3b'
down_revision: Union[str, None] = '1c97dcc94f1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sauces', 'Recipe')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sauces', sa.Column('Recipe', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###
