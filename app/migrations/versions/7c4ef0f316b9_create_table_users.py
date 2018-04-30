"""Create table users

Revision ID: 7c4ef0f316b9
Revises: 
Create Date: 2018-04-30 14:24:00.269246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4ef0f316b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('users',
		sa.Column('id', sa.Integer(), nullable=False),
		sa.PrimaryKeyConstraint('id')
	)


def downgrade():
    op.drop_table('users')
