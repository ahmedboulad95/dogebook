"""Initial migration

Revision ID: 23939bfa4ace
Revises: 
Create Date: 2021-06-12 19:23:21.676388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23939bfa4ace'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('your_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('your_model')
    # ### end Alembic commands ###
