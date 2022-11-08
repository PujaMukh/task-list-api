"""empty message

Revision ID: 014260957d84
Revises: 56b3c36fe8a6
Create Date: 2022-11-08 13:22:57.240318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '014260957d84'
down_revision = '56b3c36fe8a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###