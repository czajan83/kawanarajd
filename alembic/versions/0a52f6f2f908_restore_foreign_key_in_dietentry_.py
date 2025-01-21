"""restore foreign key in dietentry database

Revision ID: 0a52f6f2f908
Revises: 5380fb8c5406
Create Date: 2025-01-21 16:09:49.227321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a52f6f2f908'
down_revision: Union[str, None] = '5380fb8c5406'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'dietentry', 'dishes', ['food_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dietentry', type_='foreignkey')
    # ### end Alembic commands ###
