"""creating url table

Revision ID: e14be8fa3b04
Revises: 
Create Date: 2024-11-03 22:21:15.160613

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e14be8fa3b04"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "url",
        sa.Column("token", sa.String(), nullable=False),
        sa.Column("url", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("token"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("url")
    # ### end Alembic commands ###
