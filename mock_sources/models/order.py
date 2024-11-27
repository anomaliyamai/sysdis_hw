import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class Order(DeclBase):
    __tablename__ = 'orders'

    id = sa.Column(sa.String, primary_key=True)
    user_id = sa.Column(sa.Integer)
    zone_id = sa.Column(sa.Integer)
    base_coin_amount = sa.Column(sa.Float)
