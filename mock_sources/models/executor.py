import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class Executor(DeclBase):
    id = sa.Column(sa.Integer)
    tags = sa.Column(sa.JSON)
    rating = sa.Column(sa.Float)
