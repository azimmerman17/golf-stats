"""Initial Migration of the course model

Revision ID: 18d7e6d04288
Revises: 738fd119aceb
Create Date: 2025-10-26 17:57:25.688751

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '18d7e6d04288'
down_revision = '738fd119aceb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Course',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('facility_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('hole_count', sa.Integer(), server_default='18', nullable=False),
    sa.Column('established', sa.Integer(), nullable=True),
    sa.Column('architect', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('NOW()'), nullable=False),
    sa.ForeignKeyConstraint(['facility_id'], ['Facility.facility_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('course_id'),
    sa.UniqueConstraint('course_id')
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('Course')
    # ### end Alembic commands ###
