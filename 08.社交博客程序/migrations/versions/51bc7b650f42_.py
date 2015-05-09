"""empty message

Revision ID: 51bc7b650f42
Revises: 378e931e5ff4
Create Date: 2015-05-08 18:59:57.455000

"""

# revision identifiers, used by Alembic.
revision = '51bc7b650f42'
down_revision = '378e931e5ff4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    ### end Alembic commands ###
