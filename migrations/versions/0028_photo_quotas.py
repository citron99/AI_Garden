"""Track photo size for quotas and orphan cleanup.

Revision ID: 0028_photo_quotas
Revises: 0027_refresh_reuse
"""

from alembic import op
import sqlalchemy as sa


revision = "0028_photo_quotas"
down_revision = "0027_refresh_reuse"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("plant_photos") as batch:
        batch.add_column(sa.Column("size_bytes", sa.Integer(), nullable=False, server_default="0"))


def downgrade() -> None:
    with op.batch_alter_table("plant_photos") as batch:
        batch.drop_column("size_bytes")
