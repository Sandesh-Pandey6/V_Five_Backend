"""admin user roles

Revision ID: 005
Revises: 004
Create Date: 2026-06-03

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "005"
down_revision: Union[str, Sequence[str], None] = "004"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "admin_users",
        sa.Column(
            "role",
            sa.String(length=32),
            nullable=False,
            server_default="user",
        ),
    )
    # First seeded account is the primary administrator.
    op.execute(
        sa.text(
            """
            UPDATE admin_users
            SET role = 'superadmin'
            WHERE id = (SELECT MIN(id) FROM admin_users)
            """
        )
    )


def downgrade() -> None:
    op.drop_column("admin_users", "role")
