"""empty message

Revision ID: 6ec7e5fc8411
Revises: 27685bb04244
Create Date: 2019-08-26 13:25:19.235287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ec7e5fc8411'
down_revision = '27685bb04244'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('event_user_id_fkey', 'event', type_='foreignkey')
    op.drop_column('event', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('event_user_id_fkey', 'event', 'user', ['user_id'], ['id'])
    op.drop_table('user_event')
    # ### end Alembic commands ###