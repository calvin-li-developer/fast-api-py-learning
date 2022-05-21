"""Create Post Table

Revision ID: 8287b2cfc6b5
Revises: 
Create Date: 2022-05-20 19:26:39.292709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8287b2cfc6b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
