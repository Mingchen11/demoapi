"""create posts table

Revision ID: 805681bfe39a
Revises: 
Create Date: 2022-08-03 12:21:48.808641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '805681bfe39a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
    pass
