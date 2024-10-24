"""add bool

Revision ID: 8f5f50ea40ab
Revises: 91368be0ff1d
Create Date: 2024-08-28 21:49:16.608352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f5f50ea40ab'
down_revision: Union[str, None] = '91368be0ff1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
