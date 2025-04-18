"""Create movies table

Revision ID: ca50c94bd302
Revises: 
Create Date: 2025-04-13 16:57:05.495559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca50c94bd302'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('poster', sa.String(length=120), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie')
    # ### end Alembic commands ###
