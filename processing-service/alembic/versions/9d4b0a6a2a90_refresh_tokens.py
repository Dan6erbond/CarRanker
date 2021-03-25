"""refresh tokens

Revision ID: 9d4b0a6a2a90
Revises: 70f9004081c9
Create Date: 2021-03-22 19:29:05.614591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d4b0a6a2a90'
down_revision = '70f9004081c9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('refresh_tokens',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.Column('date_modified', sa.DateTime(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('is_revoked', sa.Boolean(), nullable=False),
                    sa.Column('expires', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('refresh_tokens')
