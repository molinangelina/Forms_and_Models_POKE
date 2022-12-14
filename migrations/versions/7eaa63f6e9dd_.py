"""empty message

Revision ID: 7eaa63f6e9dd
Revises: 
Create Date: 2022-07-28 22:29:24.285684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eaa63f6e9dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poke',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poke_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('poke_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poke')
    # ### end Alembic commands ###
