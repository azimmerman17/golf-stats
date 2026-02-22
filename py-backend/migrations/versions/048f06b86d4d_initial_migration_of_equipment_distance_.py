"""Initial migration of equipment distance model

Revision ID: 048f06b86d4d
Revises: 3d2ad1c26047
Create Date: 2026-02-22 15:38:29.994552

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '048f06b86d4d'
down_revision = '3d2ad1c26047'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Equipment_Distance',
    sa.Column('equipment_distance_id', sa.Integer(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.Column('manual_max_distance', sa.FLOAT(), nullable=True),
    sa.Column('manual_stock_distance', sa.FLOAT(), nullable=True),
    sa.Column('manual_knockdown_distance', sa.FLOAT(), nullable=True),
    sa.Column('manual_shoulder_distance', sa.FLOAT(), nullable=True),
    sa.Column('manual_hip_distance', sa.FLOAT(), nullable=True),
    sa.Column('manual_knee_distance', sa.FLOAT(), nullable=True),
    sa.Column('manual_dispersion', sa.FLOAT(), nullable=True),
    sa.Column('calc_max_distance', sa.FLOAT(), nullable=True),
    sa.Column('calc_stock_distance', sa.FLOAT(), nullable=True),
    sa.Column('calc_knockdown_distance', sa.FLOAT(), nullable=True),
    sa.Column('calc_shoulder_distance', sa.FLOAT(), nullable=True),
    sa.Column('calc_hip_distance', sa.FLOAT(), nullable=True),
    sa.Column('calc_knee_distance', sa.FLOAT(), nullable=True),
    sa.Column('calc_dispersion', sa.FLOAT(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['equipment_id'], ['Equipment.equipment_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('equipment_distance_id'),
    sa.UniqueConstraint('equipment_distance_id')
    )

def downgrade():
    op.drop_table('Equipment_Distance')
