"""add account_confirmed column to user with otp columns

Revision ID: 73a49e34449c
Revises: 66948580bf0d
Create Date: 2024-09-30 21:33:44.306460

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "73a49e34449c"
down_revision: Union[str, None] = "66948580bf0d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("users", sa.Column("otp", sa.String(), nullable=True))
    op.add_column("users", sa.Column("otp_expiration", sa.DateTime(), nullable=True))
    op.add_column(
        "users",
        sa.Column(
            "account_confirmed", sa.Boolean(), nullable=False, server_default="False"
        ),
    )


def downgrade():
    op.drop_column("users", "otp")
    op.drop_column("users", "otp_expiration")
    op.drop_column("users", "account_confirmed")
