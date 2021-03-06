"""allow comment field in rich text table

Revision ID: 5d568739cef8
Revises: 91c99f5d8832
Create Date: 2021-05-18 11:29:07.390916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d568739cef8'
down_revision = '91c99f5d8832'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rich_text_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_comment', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rich_text_post', schema=None) as batch_op:
        batch_op.drop_column('allowed_comment')

    # ### end Alembic commands ###
