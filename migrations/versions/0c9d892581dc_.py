"""empty message

Revision ID: 0c9d892581dc
Revises: 7f3fe2a68d69
Create Date: 2025-01-22 19:33:26.371070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c9d892581dc'
down_revision = '7f3fe2a68d69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'planet', ['homeworld_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('homeworld_id')

    # ### end Alembic commands ###
