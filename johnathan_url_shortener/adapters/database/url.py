from sqlalchemy import Table, Column, String

from johnathan_url_shortener.adapters.database.metadata import metadata


URL = Table(
    "url",
    metadata,
    Column("token", String, primary_key=True),
    Column("url", String),
)
