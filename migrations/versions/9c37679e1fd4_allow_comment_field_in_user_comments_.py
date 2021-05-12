"""allow comment field in user comments table

Revision ID: 9c37679e1fd4
Revises: 45a95499eda8
Create Date: 2021-05-12 18:42:40.344287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c37679e1fd4'
down_revision = '45a95499eda8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_comments_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_comment', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_comments_post', schema=None) as batch_op:
        batch_op.drop_column('allowed_comment')

    # ### end Alembic commands ###
