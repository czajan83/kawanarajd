"""added recipe 500 characters varchar column

Revision ID: 97c2b0524723
Revises: 53a38baf8a3b
Create Date: 2025-01-17 15:17:39.974772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97c2b0524723'
down_revision: Union[str, None] = '53a38baf8a3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sauces', sa.Column('recipe', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sauces', 'recipe')
    # ### end Alembic commands ###