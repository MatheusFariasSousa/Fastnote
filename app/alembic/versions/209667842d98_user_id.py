"""user id

Revision ID: 209667842d98
Revises: aabe4bd09fa0
Create Date: 2024-09-20 19:02:17.424038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '209667842d98'
down_revision: Union[str, None] = 'aabe4bd09fa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
