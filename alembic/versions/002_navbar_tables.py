"""create per-navbar CMS tables (home, courses, destinations, study_abroad, about_us, contact_us)

Revision ID: 002
Revises: 001
Create Date: 2026-06-03

"""

import json
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "002"
down_revision: Union[str, Sequence[str], None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

NAVBAR_TABLES = ("home", "courses", "destinations", "study_abroad", "about_us", "contact_us")

KEY_TO_TABLE = {
    "home": "home",
    "courses": "courses",
    "destinations": "destinations",
    "studyAbroad": "study_abroad",
    "about": "about_us",
    "contact": "contact_us",
}


def _cms_page_columns():
    return [
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("data", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    ]


def upgrade() -> None:
    for table in NAVBAR_TABLES:
        op.create_table(table, *_cms_page_columns(), sa.PrimaryKeyConstraint("id"))

    conn = op.get_bind()
    inspector = sa.inspect(conn)
    if "cms_sections" not in inspector.get_table_names():
        return

    rows = conn.execute(sa.text("SELECT key, data FROM cms_sections")).fetchall()
    for key, data in rows:
        table = KEY_TO_TABLE.get(key)
        if table and data is not None:
            conn.execute(
                sa.text(f'INSERT INTO "{table}" (data) VALUES (CAST(:payload AS jsonb))'),
                {"payload": json.dumps(data)},
            )

    op.drop_index("ix_cms_sections_key", table_name="cms_sections")
    op.drop_table("cms_sections")


def downgrade() -> None:
    op.create_table(
        "cms_sections",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("key", sa.String(length=64), nullable=False),
        sa.Column("data", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    op.create_index("ix_cms_sections_key", "cms_sections", ["key"], unique=True)

    TABLE_TO_KEY = {v: k for k, v in KEY_TO_TABLE.items()}
    conn = op.get_bind()

    for table in NAVBAR_TABLES:
        row = conn.execute(sa.text(f'SELECT data FROM "{table}" ORDER BY id LIMIT 1')).fetchone()
        if row:
            conn.execute(
                sa.text(
                    "INSERT INTO cms_sections (key, data) VALUES (:key, CAST(:payload AS jsonb))"
                ),
                {"key": TABLE_TO_KEY[table], "payload": json.dumps(row[0])},
            )
        op.drop_table(table)
