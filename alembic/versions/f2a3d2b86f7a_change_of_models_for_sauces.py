"""change of models for Sauces

Revision ID: f2a3d2b86f7a
Revises: 6021593f4c4c
Create Date: 2025-01-17 15:06:13.616512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f2a3d2b86f7a'
down_revision: Union[str, None] = '6021593f4c4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sauces', sa.Column('Recipe', sa.String(length=50), nullable=False))
    op.drop_constraint('sauces_ibfk_2', 'sauces', type_='foreignkey')
    op.drop_constraint('sauces_ibfk_3', 'sauces', type_='foreignkey')
    op.drop_constraint('sauces_ibfk_4', 'sauces', type_='foreignkey')
    op.drop_constraint('sauces_ibfk_1', 'sauces', type_='foreignkey')
    op.drop_column('sauces', 'ingr4_amount')
    op.drop_column('sauces', 'ingr3_amount')
    op.drop_column('sauces', 'ingr1_id')
    op.drop_column('sauces', 'ingr2_id')
    op.drop_column('sauces', 'ingr2_amount')
    op.drop_column('sauces', 'ingr4_id')
    op.drop_column('sauces', 'ingr3_id')
    op.drop_column('sauces', 'ingr1_amount')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sauces', sa.Column('ingr1_amount', mysql.FLOAT(), nullable=False))
    op.add_column('sauces', sa.Column('ingr3_id', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('sauces', sa.Column('ingr4_id', mysql.VARCHAR(length=32), nullable=True))
    op.add_column('sauces', sa.Column('ingr2_amount', mysql.FLOAT(), nullable=False))
    op.add_column('sauces', sa.Column('ingr2_id', mysql.VARCHAR(length=32), nullable=False))
    op.add_column('sauces', sa.Column('ingr1_id', mysql.VARCHAR(length=32), nullable=False))
    op.add_column('sauces', sa.Column('ingr3_amount', mysql.FLOAT(), nullable=True))
    op.add_column('sauces', sa.Column('ingr4_amount', mysql.FLOAT(), nullable=True))
    op.create_foreign_key('sauces_ibfk_1', 'sauces', 'raws', ['ingr1_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('sauces_ibfk_4', 'sauces', 'raws', ['ingr4_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('sauces_ibfk_3', 'sauces', 'raws', ['ingr3_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('sauces_ibfk_2', 'sauces', 'raws', ['ingr2_id'], ['id'], ondelete='CASCADE')
    op.drop_column('sauces', 'Recipe')
    # ### end Alembic commands ###
