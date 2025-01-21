"""change column type for table dietentry added at to datetime

Revision ID: c39e94e9358f
Revises: 72236245c9b8
Create Date: 2025-01-21 15:40:00.865548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c39e94e9358f'
down_revision: Union[str, None] = '72236245c9b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sauces')
    op.alter_column('dietentry', 'added_at',
               existing_type=mysql.VARCHAR(length=24),
               type_=sa.DateTime(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dietentry', 'added_at',
               existing_type=sa.DateTime(),
               type_=mysql.VARCHAR(length=24),
               existing_nullable=True)
    op.create_table('sauces',
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
    sa.Column('recipe', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('final_amount_in_grams', mysql.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
