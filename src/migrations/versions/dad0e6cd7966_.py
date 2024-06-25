"""empty message

Revision ID: dad0e6cd7966
Revises: b5ac87aef5dc
Create Date: 2024-06-19 20:56:42.583530

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dad0e6cd7966"
down_revision: Union[str, None] = "b5ac87aef5dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("authors", sa.Column("middle_name", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("authors", "middle_name")
    # ### end Alembic commands ###
