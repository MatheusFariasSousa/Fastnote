"""create note table

Revision ID: 7d1520c0cb97
Revises: 2c2bdea1817c
Create Date: 2024-08-28 21:43:39.646487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d1520c0cb97'
down_revision: Union[str, None] = '2c2bdea1817c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
