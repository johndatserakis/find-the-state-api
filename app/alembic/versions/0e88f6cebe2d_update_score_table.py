"""Update score table

Revision ID: 0e88f6cebe2d
Revises: a1c5591554f0
Create Date: 2021-05-03 18:52:27.262214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0e88f6cebe2d"
down_revision = "a1c5591554f0"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "scores",
        sa.Column("streak_high", sa.Integer, nullable=False, server_default="0"),
    )


def downgrade():
    op.drop_column("scores", "streak_high")
