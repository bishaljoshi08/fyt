"""mycourse created

Revision ID: 040778c46855
Revises: 0b443240aacd
Create Date: 2020-09-02 09:55:37.527539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040778c46855'
down_revision = '0b443240aacd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mycourse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('cost', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mycourse')
    # ### end Alembic commands ###
