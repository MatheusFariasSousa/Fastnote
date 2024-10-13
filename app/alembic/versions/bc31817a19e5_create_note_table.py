"""create note table

Revision ID: bc31817a19e5
Revises: 57fdd62d5d84
Create Date: 2024-08-28 20:43:51.934919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc31817a19e5'
down_revision: Union[str, None] = '57fdd62d5d84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
