"""empty message

Revision ID: 4a7b2c5c6bf9
Revises: 
Create Date: 2024-02-23 07:22:39.331697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7b2c5c6bf9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('houses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=256), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('houses')
    # ### end Alembic commands ###
