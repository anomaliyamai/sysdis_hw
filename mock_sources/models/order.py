import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class Order(DeclBase):
    id = sa.Column(sa.Integer)
    user_id = sa.Column(sa.Integer)
    zone_id = sa.Column(sa.Integer)
    base_coin_amount = sa.Column(sa.Float)
