import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class Zone(DeclBase):
    __tablename__ = 'zones'

    id = sa.Column(sa.Integer, primary_key=True)
    coin_coeff = sa.Column(sa.Float)
    display_name = sa.Column(sa.String)
