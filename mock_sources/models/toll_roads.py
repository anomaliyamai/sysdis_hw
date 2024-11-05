import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class TollRoad(DeclBase):
    bonus_amount = sa.Column(sa.Float)
