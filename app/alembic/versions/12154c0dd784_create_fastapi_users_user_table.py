"""Create FastAPI-Users user table

Revision ID: 12154c0dd784
Revises: a6517320e072
Create Date: 2021-04-23 15:59:22.346539

"""
from alembic import op
import sqlalchemy as sa

# from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "12154c0dd784"
down_revision = "a6517320e072"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",  # Modified from the original FastAPI-Users `user` table name
        sa.Column(
            "id",
            UUID(as_uuid=True),  # Modified from the original FastAPI-Users `UUID` type
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
        ),
        sa.Column(
            "email", sa.String(length=320), unique=True, index=True, nullable=False
        ),
        sa.Column("hashed_password", sa.String(length=72), nullable=False),
        sa.Column("is_active", sa.Boolean, default=True, nullable=False),
        sa.Column("is_superuser", sa.Boolean, default=False, nullable=False),
        sa.Column("is_verified", sa.Boolean, default=False, nullable=False),
    )


def downgrade():
    op.drop_table("users")
