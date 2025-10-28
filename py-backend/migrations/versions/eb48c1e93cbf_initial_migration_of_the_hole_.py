"""Initial Migration of the hole model

Revision ID: eb48c1e93cbf
Revises: 39871f8fd94b
Create Date: 2025-10-28 04:44:13.860339

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eb48c1e93cbf'
down_revision = '39871f8fd94b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Hole',
    sa.Column('hole_id', sa.Integer(), nullable=False),
    sa.Column('tee_id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('yards', sa.Integer(), server_default='400', nullable=False),
    sa.Column('meters', sa.Integer(), server_default='367', nullable=False),
    sa.Column('par_male', sa.Integer(), nullable=True),
    sa.Column('si_male', sa.Integer(), nullable=True),
    sa.Column('par_female', sa.Integer(), nullable=True),
    sa.Column('si_female', sa.Integer(), nullable=True),
    sa.Column('effective_date', sa.DATE(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['tee_id'], ['Tee.tee_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('hole_id'),
    sa.CheckConstraint('number >= 1 AND number <= 18', name=op.f('check_hole_number')),
    sa.CheckConstraint('yards > 0 AND yards <= 999', name=op.f('check_hole_yards')),
    sa.CheckConstraint('meters > 0 AND meters <= 999', name=op.f('check_hole_meters')),
    sa.CheckConstraint('par_male >= 3 AND par_male <= 6', name=op.f('check_hole_par_male')),
    sa.CheckConstraint('par_female >= 3 AND par_female <= 6', name=op.f('check_hole_par_female')),
    sa.CheckConstraint('si_male >= 1 AND si_male <= 18', name=op.f('check_hole_si_male')),
    sa.CheckConstraint('si_female >= 1 AND si_female <= 18', name=op.f('check_hole_si_female')),
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('Hole')
    # ### end Alembic commands ###
