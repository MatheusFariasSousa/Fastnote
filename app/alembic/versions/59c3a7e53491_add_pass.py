"""add pass

Revision ID: 59c3a7e53491
Revises: 57be44e6f3d9
Create Date: 2024-08-28 21:52:26.932959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59c3a7e53491'
down_revision: Union[str, None] = '57be44e6f3d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
