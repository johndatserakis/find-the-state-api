"""Create state table

Revision ID: 589f4c4cdef2
Revises:
Create Date: 2021-04-03 20:32:21.216053

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

# revision identifiers, used by Alembic.
revision = "589f4c4cdef2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "states",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("name", sa.String, unique=True, index=True, nullable=False),
        sa.Column("summary", sa.String, index=True, nullable=False),
        sa.Column("link", sa.String, index=True, nullable=False),
        sa.Column("image", sa.String, index=True, nullable=False),
        sa.Column("created_date", sa.DateTime, default=func.now(), nullable=False),
    )


def downgrade():
    op.drop_table("states")
