import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class TollRoad(DeclBase):
    __tablename__ = 'tollroads'

    id = sa.Column(sa.String, primary_key=True)
    bonus_amount = sa.Column(sa.Float)
