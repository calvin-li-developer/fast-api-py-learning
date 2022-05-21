"""add content column to post table

Revision ID: 52de721564ef
Revises: 8287b2cfc6b5
Create Date: 2022-05-20 19:31:55.026597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52de721564ef'
down_revision = '8287b2cfc6b5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
