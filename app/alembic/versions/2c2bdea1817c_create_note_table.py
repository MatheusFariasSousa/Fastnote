"""create note table

Revision ID: 2c2bdea1817c
Revises: bc31817a19e5
Create Date: 2024-08-28 20:47:27.236339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c2bdea1817c'
down_revision: Union[str, None] = 'bc31817a19e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
