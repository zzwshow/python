"""empty message

Revision ID: 2132c74dedd1
Revises: 
Create Date: 2018-02-08 13:42:19.802360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2132c74dedd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=50), nullable=False),
    sa.Column('project_area', sa.String(length=50), nullable=False),
    sa.Column('project_description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hosts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host_name', sa.String(length=100), nullable=False),
    sa.Column('public_address', sa.String(length=100), nullable=False),
    sa.Column('private_address', sa.String(length=100), nullable=False),
    sa.Column('os', sa.String(length=50), nullable=False),
    sa.Column('host_description', sa.Text(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hosts')
    op.drop_table('users')
    op.drop_table('project')
    # ### end Alembic commands ###
