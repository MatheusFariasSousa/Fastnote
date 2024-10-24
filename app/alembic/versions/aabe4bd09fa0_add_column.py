"""add column

Revision ID: aabe4bd09fa0
Revises: 59c3a7e53491
Create Date: 2024-08-28 21:56:14.493427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aabe4bd09fa0'
down_revision: Union[str, None] = '59c3a7e53491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
