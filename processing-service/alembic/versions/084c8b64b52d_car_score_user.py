"""car score user

Revision ID: 084c8b64b52d
Revises: 9d4b0a6a2a90
Create Date: 2021-03-22 19:32:33.061604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '084c8b64b52d'
down_revision = '9d4b0a6a2a90'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('car_scores',
                  sa.Column('user_id', sa.Integer(), nullable=False),
                  )
    op.create_foreign_key(
        'fk_car_score_user', 'car_scores',
        'users', ['user_id'], ['id']
    )


def downgrade():
    pass
