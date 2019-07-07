import sqlalchemy as sa


convention = {
  "ix": 'ix_%(column_0_label)s',
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = sa.MetaData(naming_convention=convention)


AuthTable = sa.Table(
    'auth',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('user_id', sa.ForeignKey('users.id'), nullable=False, index=True)
)


UsersTable = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False)
)
