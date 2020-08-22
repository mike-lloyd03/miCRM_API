"""contact table

Revision ID: fd2205cc6dd8
Revises: 
Create Date: 2020-08-18 22:59:54.185199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd2205cc6dd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('business', sa.String(length=240), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('client_type', sa.String(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_first_name'), 'contact', ['first_name'], unique=False)
    op.create_index(op.f('ix_contact_last_name'), 'contact', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contact_last_name'), table_name='contact')
    op.drop_index(op.f('ix_contact_first_name'), table_name='contact')
    op.drop_table('contact')
    # ### end Alembic commands ###