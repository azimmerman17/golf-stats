"""Initial Migration of the tee model

Revision ID: f6e84044cdd3
Revises: 18d7e6d04288
Create Date: 2025-10-27 20:18:58.802399

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f6e84044cdd3'
down_revision = '18d7e6d04288'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Tee',
    sa.Column('tee_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('yards', sa.Integer(), server_default='7200', nullable=False),
    sa.Column('meters', sa.Integer(), server_default='6600', nullable=False),
    sa.Column('hole_count', sa.Integer(), server_default='18', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['Course.course_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('tee_id'),
    sa.CheckConstraint('yards > 0', name=op.f('check_tee_yards')),
    sa.CheckConstraint('meters > 0', name=op.f('check_tee_meters')),
    sa.CheckConstraint('hole_count >= 1 AND hole_count <= 18', name=op.f('check_tee_hole_count')),
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('Tee')
    # ### end Alembic commands ###
