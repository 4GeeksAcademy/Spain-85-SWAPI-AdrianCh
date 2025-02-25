"""empty message

Revision ID: c71f329c8ca3
Revises: 6d50f0df0d60
Create Date: 2025-01-24 19:28:39.721165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c71f329c8ca3'
down_revision = '6d50f0df0d60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld_name', sa.Integer(), nullable=False))
        batch_op.drop_constraint('character_homeworld_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planet', ['homeworld_name'], ['name'])
        batch_op.drop_column('homeworld_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('character_homeworld_id_fkey', 'planet', ['homeworld_id'], ['id'])
        batch_op.drop_column('homeworld_name')

    # ### end Alembic commands ###
