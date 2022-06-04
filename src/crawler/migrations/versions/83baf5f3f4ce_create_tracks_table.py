# type: ignore

"""Create tracks table.

Revision ID: 83baf5f3f4ce
Revises:
Create Date: 2021-12-16 20:08:17.486039

"""
import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "83baf5f3f4ce"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    schema_upgrade()
    if context.get_x_argument(as_dictionary=True).get("data"):
        data_upgrade()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get("data"):
        data_downgrade()
    schema_downgrade()


def schema_upgrade():
    op.create_table(
        "tracks",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("is_discarded", sa.Boolean(), nullable=False),
        sa.Column("registered_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("artist", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="crawler",
    )


def schema_downgrade():
    op.drop_table("tracks", schema="crawler")


def data_upgrade():
    pass


def data_downgrade():
    pass
