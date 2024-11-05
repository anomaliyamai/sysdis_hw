import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class Zone(DeclBase):
    id = sa.Column(sa.Integer)
    coin_coeff = sa.Column(sa.Float)
    display_name = sa.Column(sa.String)
