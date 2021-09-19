"""empty message

Revision ID: 605687849d3c
Revises: eecca008e169
Create Date: 2021-07-09 12:37:01.679666

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '605687849d3c'
down_revision = 'eecca008e169'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('logo_size', sa.Integer(), server_default='1000', nullable=False))
    op.add_column('settings', sa.Column('image_size', sa.Integer(), server_default='10000', nullable=False))
    op.add_column('settings', sa.Column('slide_size', sa.Integer(), server_default='20000', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'slide_size')
    op.drop_column('settings', 'image_size')
    op.drop_column('settings', 'logo_size')
    # ### end Alembic commands ###