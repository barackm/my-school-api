"""remove_enrollment_date_from_user_enrollments

Revision ID: 66948580bf0d
Revises: 15f40949099c
Create Date: 2024-09-13 00:31:46.527699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66948580bf0d'
down_revision: Union[str, None] = '15f40949099c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('user_enrollments', 'enrollment_date')
    pass


def downgrade() -> None:
    op.add_column('user_enrollments', sa.Column('enrollment_date', sa.DateTime(), nullable=False))
    pass
