"""Initial migration of equipment model

Revision ID: 23b1f9915e84
Revises: e10b3932e9d5
Create Date: 2026-02-22 08:19:18.490652

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '23b1f9915e84'
down_revision = 'e10b3932e9d5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Equipment',
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('catagory', sa.Enum('Driver', 'Wood', 'Hybrid', 'Iron', 'Wedge', 'Putter', name='equipment_type'), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('short_name', sa.String(length=3), nullable=False),
    sa.Column('make', sa.String(length=25), nullable=False),
    sa.Column('model', sa.String(length=25), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['Person.person_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('equipment_id'),
    sa.UniqueConstraint('equipment_id')
    )
def downgrade():
    op.drop_table('Equipment')
    # ### end Alembic commands ###
