"""Bug Fix

Revision ID: 4679e6954b87
Revises: 93f1d2c5c1d5
Create Date: 2024-01-16 16:30:59.121074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4679e6954b87'
down_revision = '93f1d2c5c1d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscriptions')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_id')

    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_id', ['id'], unique=False)

    op.create_table('subscriptions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('website', sa.VARCHAR(), nullable=False),
    sa.Column('price', sa.NUMERIC(precision=10, scale=2), nullable=False),
    sa.Column('start_date', sa.DATETIME(), nullable=False),
    sa.Column('end_date', sa.DATETIME(), nullable=False),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_subscription_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###