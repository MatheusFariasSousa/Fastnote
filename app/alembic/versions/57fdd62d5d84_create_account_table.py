"""create account table

Revision ID: 57fdd62d5d84
Revises: 97835f78a477
Create Date: 2024-08-28 20:21:08.412850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57fdd62d5d84'
down_revision: Union[str, None] = '97835f78a477'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
