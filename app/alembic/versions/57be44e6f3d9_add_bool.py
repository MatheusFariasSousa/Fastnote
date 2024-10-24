"""add bool

Revision ID: 57be44e6f3d9
Revises: 8f5f50ea40ab
Create Date: 2024-08-28 21:50:59.669708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57be44e6f3d9'
down_revision: Union[str, None] = '8f5f50ea40ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
