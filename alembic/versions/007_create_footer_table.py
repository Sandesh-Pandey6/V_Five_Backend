"""create footer CMS table and migrate footerDescription from home

Revision ID: 007
Revises: 006
Create Date: 2026-06-03

"""

import json
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "007"
down_revision: Union[str, Sequence[str], None] = "006"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_FOOTER = {
    "brandTitle": "About Us",
    "description": (
        "V Five is a leading education consultancy dedicated to fulfilling your dreams of "
        "international education and career success through expert mentoring and unwavering support."
    ),
    "quickLinksTitle": "Quick Links",
    "quickLinks": [
        {"label": "Home", "href": "/"},
        {"label": "About Us", "href": "/about"},
        {"label": "Courses", "href": "/courses"},
        {"label": "Destinations", "href": "/destinations"},
        {"label": "Study Abroad", "href": "/study-abroad"},
        {"label": "Contact Us", "href": "/contact"},
    ],
    "supportTitle": "Support",
    "supportLinks": [
        {"label": "Privacy Policy", "href": "#"},
        {"label": "Terms of Service", "href": "#"},
        {"label": "FAQ", "href": "#"},
        {"label": "Career Guidance", "href": "/contact"},
    ],
    "contactTitle": "Contact Info",
    "copyrightText": "V Five Education Consultancy. All rights reserved.",
    "taglinePrefix": "Designed with Excellence for",
    "taglineHighlight": "Future Global Scholars",
}


def upgrade() -> None:
    op.create_table(
        "footer",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("data", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    conn = op.get_bind()
    footer_payload = dict(DEFAULT_FOOTER)

    home_row = conn.execute(sa.text('SELECT id, data FROM "home" ORDER BY id LIMIT 1')).fetchone()
    if home_row is not None:
        home_id, home_data = home_row[0], dict(home_row[1])
        legacy_desc = home_data.pop("footerDescription", None)
        if legacy_desc:
            footer_payload["description"] = legacy_desc
        conn.execute(
            sa.text('UPDATE "home" SET data = CAST(:payload AS jsonb) WHERE id = :id'),
            {"payload": json.dumps(home_data), "id": home_id},
        )

    conn.execute(
        sa.text('INSERT INTO "footer" (data) VALUES (CAST(:payload AS jsonb))'),
        {"payload": json.dumps(footer_payload)},
    )


def downgrade() -> None:
    conn = op.get_bind()
    footer_row = conn.execute(
        sa.text('SELECT data FROM "footer" ORDER BY id LIMIT 1')
    ).fetchone()

    if footer_row is not None:
        footer_data = dict(footer_row[0])
        description = footer_data.get("description", "")
        home_row = conn.execute(sa.text('SELECT id, data FROM "home" ORDER BY id LIMIT 1')).fetchone()
        if home_row is not None:
            home_id, home_data = home_row[0], dict(home_row[1])
            home_data["footerDescription"] = description
            conn.execute(
                sa.text('UPDATE "home" SET data = CAST(:payload AS jsonb) WHERE id = :id'),
                {"payload": json.dumps(home_data), "id": home_id},
            )

    op.drop_table("footer")
