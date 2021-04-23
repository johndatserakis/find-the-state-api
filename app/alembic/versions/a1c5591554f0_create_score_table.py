"""Create score table

Revision ID: a1c5591554f0
Revises: a6517320e072
Create Date: 2021-04-23 23:09:22.801565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "a1c5591554f0"
down_revision = "a6517320e072"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "scores",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column("score", sa.String, index=True, nullable=False),
        sa.Column("updated_date", sa.DateTime),
        sa.Column(
            "created_date", sa.DateTime, server_default=sa.text("now()"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("scores")
