"""add content column to posts table

Revision ID: 18e1fca3914f
Revises: 229fc1c1f123
Create Date: 2022-06-10 06:53:18.598871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18e1fca3914f'
down_revision = '229fc1c1f123'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
