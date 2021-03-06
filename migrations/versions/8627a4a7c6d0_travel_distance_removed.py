"""travel distance removed

Revision ID: 8627a4a7c6d0
Revises: 143889679711
Create Date: 2020-09-14 13:56:38.380558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8627a4a7c6d0'
down_revision = '143889679711'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_column('travel_distance')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.add_column(sa.Column('travel_distance', sa.VARCHAR(length=64), nullable=True))

    # ### end Alembic commands ###
