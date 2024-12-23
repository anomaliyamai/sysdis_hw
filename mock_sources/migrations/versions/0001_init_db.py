"""init_db

Revision ID: 0001
Revises: 
Create Date: 2024-11-09 15:56:52.109051

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
    # op.create_table('config_map',)
    op.create_table('executors',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=False),
    sa.Column('base_coin_amount', sa.Float()),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tollroads',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('bonus_amount', sa.Float()),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zones',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('coin_coeff', sa.Float()),
    sa.Column('display_name', sa.String()),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('config_map')
    op.drop_table('executors')
    op.drop_table('orders')
    op.drop_table('tollroads')
    op.drop_table('zones')
    # ### end Alembic commands ###
