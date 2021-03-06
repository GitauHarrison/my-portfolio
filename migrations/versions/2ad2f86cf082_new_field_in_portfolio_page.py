"""new field in portfolio page

Revision ID: 2ad2f86cf082
Revises: b2b3cc7e438f
Create Date: 2021-04-30 12:44:43.059947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ad2f86cf082'
down_revision = 'b2b3cc7e438f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolio_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_project', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolio_list', schema=None) as batch_op:
        batch_op.drop_column('allowed_project')

    # ### end Alembic commands ###
