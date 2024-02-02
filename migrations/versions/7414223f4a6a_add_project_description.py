"""Add project description

Revision ID: 7414223f4a6a
Revises: f11fd270b732
Create Date: 2024-02-02 09:24:02.136432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7414223f4a6a'
down_revision = 'f11fd270b732'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###