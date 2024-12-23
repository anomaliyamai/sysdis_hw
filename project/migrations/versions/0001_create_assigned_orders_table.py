"""create_assigned_orders_table

Revision ID: 0001
Revises: 
Create Date: 2024-11-05 19:16:09.301654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assigned_orders',
    sa.Column('order_id', sa.String()),
    sa.Column('executor_id', sa.Integer()),
    sa.Column('coin_coeff', sa.Float()),
    sa.Column('coin_bonus_amount', sa.Float()),
    sa.Column('final_coin_amount', sa.Float()),
    sa.Column('route_information', sa.String()),
    sa.Column('assign_time', sa.DateTime(timezone=True)),
    sa.Column('acquire_time', sa.DateTime(timezone=True)),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assigned_orders')
    # ### end Alembic commands ###
