"""create note tablee

Revision ID: 91368be0ff1d
Revises: 3238f365c682
Create Date: 2024-08-28 21:46:55.801707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91368be0ff1d'
down_revision: Union[str, None] = '3238f365c682'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
