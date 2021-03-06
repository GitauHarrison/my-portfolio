"""new field in admin table

Revision ID: 4ee665780c8a
Revises: e33dad164061
Create Date: 2021-04-30 10:27:59.434237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ee665780c8a'
down_revision = 'e33dad164061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles_list', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_articles_list_admin_id_admin'), 'admin', ['admin_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles_list', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_articles_list_admin_id_admin'), type_='foreignkey')

    # ### end Alembic commands ###
