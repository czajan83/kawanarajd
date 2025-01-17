"""Init

Revision ID: 4839a7b6d5b9
Revises: 
Create Date: 2025-01-15 16:47:38.170849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4839a7b6d5b9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('raws',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=96), nullable=False),
    sa.Column('kcal_100g', sa.Float(), nullable=False),
    sa.Column('fat', sa.Float(), nullable=False),
    sa.Column('saturated_fat', sa.Float(), nullable=False),
    sa.Column('carbohydrates', sa.Float(), nullable=False),
    sa.Column('simple_sugars', sa.Float(), nullable=False),
    sa.Column('fiber', sa.Float(), nullable=True),
    sa.Column('proteins', sa.Float(), nullable=False),
    sa.Column('salt', sa.Float(), nullable=False),
    sa.Column('cvi', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('raws')
    # ### end Alembic commands ###
