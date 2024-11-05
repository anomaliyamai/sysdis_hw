"""Модуль содержит метаданные для ORM."""
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
DeclBase = declarative_base(metadata=metadata)
