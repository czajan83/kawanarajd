"""create table recipes

Revision ID: e1416e7078e5
Revises: 2fe9b05c0c36
Create Date: 2025-01-21 11:09:43.353523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'e1416e7078e5'
down_revision: Union[str, None] = '2fe9b05c0c36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['component_id'], ['dishes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['recipe_id'], ['dishes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('raws')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('raws',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=96), nullable=False),
    sa.Column('kcal_100g', mysql.FLOAT(), nullable=False),
    sa.Column('fat', mysql.FLOAT(), nullable=False),
    sa.Column('saturated_fat', mysql.FLOAT(), nullable=False),
    sa.Column('carbohydrates', mysql.FLOAT(), nullable=False),
    sa.Column('simple_sugars', mysql.FLOAT(), nullable=False),
    sa.Column('fiber', mysql.FLOAT(), nullable=True),
    sa.Column('proteins', mysql.FLOAT(), nullable=False),
    sa.Column('salt', mysql.FLOAT(), nullable=False),
    sa.Column('cvi', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('recipes')
    # ### end Alembic commands ###
