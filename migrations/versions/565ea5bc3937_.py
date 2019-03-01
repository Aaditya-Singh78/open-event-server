"""empty message

Revision ID: 565ea5bc3937
Revises: 91ee86a38001
Create Date: 2019-02-18 15:50:18.809478

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565ea5bc3937'
down_revision = '91ee86a38001'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('is_billing_enabled', sa.Boolean()), server_default='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'is_billing_enabled')
    # ### end Alembic commands ###