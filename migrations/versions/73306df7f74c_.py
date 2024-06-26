"""empty message

Revision ID: 73306df7f74c
Revises: 2e5a6b20908d
Create Date: 2024-05-25 01:04:44.495978

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "73306df7f74c"
down_revision = "2e5a6b20908d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("message", schema=None) as batch_op:
        batch_op.drop_column("contact_method")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("message", schema=None) as batch_op:
        batch_op.add_column(sa.Column("contact_method", sa.VARCHAR(length=255), nullable=True))

    # ### end Alembic commands ###
