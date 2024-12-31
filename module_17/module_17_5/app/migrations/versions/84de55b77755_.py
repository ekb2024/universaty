"""empty message

Revision ID: 84de55b77755
Revises: c8e8b5e66f73
Create Date: 2024-12-31 15:38:34.971314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84de55b77755'
down_revision: Union[str, None] = 'c8e8b5e66f73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
