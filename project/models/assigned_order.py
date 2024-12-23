import sqlalchemy as sa

from metadata import DeclBase


class AssignedOrder(DeclBase):
    """."""

    __tablename__ = 'assigned_orders'

    # assign_order_id = sa.Column(sa.String)
    order_id = sa.Column(sa.String, primary_key=True)
    executor_id = sa.Column(sa.Integer)
    coin_coeff = sa.Column(sa.Float)
    coin_bonus_amount = sa.Column(sa.Float)
    final_coin_amount = sa.Column(sa.Float)
    route_information = sa.Column(sa.String)
    assign_time = sa.Column(sa.DateTime(timezone=True))
    acquire_time = sa.Column(sa.DateTime(timezone=True))
