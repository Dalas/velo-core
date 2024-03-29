"""initial migration

Revision ID: b0c4f91a0839
Revises: 
Create Date: 2019-07-07 20:52:12.880981

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b0c4f91a0839'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table(
        'auth',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_auth_user_id_users')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_auth'))
    )
    op.create_index(op.f('ix_auth_user_id'), 'auth', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auth_user_id'), table_name='auth')
    op.drop_table('auth')
    op.drop_table('users')
    # ### end Alembic commands ###
