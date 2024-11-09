import sqlalchemy as sa

from mock_sources.metadata import DeclBase


class Executor(DeclBase):
    __tablename__ = 'executors'

    id = sa.Column(sa.Integer, primary_key=True)
    tags = sa.Column(sa.JSON)
    rating = sa.Column(sa.Float)
