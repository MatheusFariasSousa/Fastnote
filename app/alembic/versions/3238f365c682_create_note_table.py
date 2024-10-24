"""create note table

Revision ID: 3238f365c682
Revises: 7d1520c0cb97
Create Date: 2024-08-28 21:46:47.602739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3238f365c682'
down_revision: Union[str, None] = '7d1520c0cb97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
