"""Add name column to users

Revision ID: 08fee3db65b9
Revises: 7c4ef0f316b9
Create Date: 2018-04-30 14:39:21.084966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08fee3db65b9'
down_revision = '7c4ef0f316b9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('name', sa.String()))


def downgrade():
    op.drop_column('users', 'name')
